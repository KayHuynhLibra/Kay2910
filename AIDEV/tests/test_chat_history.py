import pytest
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
from ai_system.core.chat_history import ChatHistory
from ai_system.core.scheduler import ChatScheduler
from ai_system.config.chat_history_config import (
    CHAT_HISTORY_DIR,
    DEFAULT_RETENTION_DAYS,
    MAX_MESSAGES_PER_FILE
)

@pytest.fixture
def chat_history():
    """Create a ChatHistory instance for testing."""
    # Create a temporary directory for testing
    test_dir = CHAT_HISTORY_DIR / "test"
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize ChatHistory with test directory
    history = ChatHistory(storage_dir=test_dir)
    yield history
    
    # Cleanup after tests
    for file in test_dir.glob("*"):
        file.unlink()
    test_dir.rmdir()

@pytest.fixture
def scheduler(chat_history):
    """Create a ChatScheduler instance for testing."""
    return ChatScheduler(chat_history)

def test_add_message(chat_history):
    """Test adding a message to chat history."""
    user_id = "test_user"
    message = "Hello, world!"
    response = "Hi there!"
    metadata = {"type": "greeting"}
    
    chat_history.add_message(user_id, message, response, metadata)
    
    # Get today's history
    today = datetime.now().date()
    history = chat_history.get_chat_history(datetime.combine(today, datetime.min.time()))
    
    assert len(history) == 1
    assert history[0]["user_id"] == user_id
    assert history[0]["message"] == message
    assert history[0]["response"] == response
    assert history[0]["metadata"] == metadata

def test_get_user_history(chat_history):
    """Test retrieving user history."""
    user_id = "test_user"
    
    # Add messages for the last 3 days
    for i in range(3):
        date = datetime.now() - timedelta(days=i)
        chat_history.add_message(
            user_id,
            f"Message {i}",
            f"Response {i}",
            {"day": i}
        )
    
    # Get user history for the last 2 days
    history = chat_history.get_user_history(user_id, days=2)
    
    assert len(history) == 2
    assert all(msg["user_id"] == user_id for msg in history)

def test_cleanup_old_history(chat_history):
    """Test cleaning up old chat history."""
    user_id = "test_user"
    
    # Add messages for the last (DEFAULT_RETENTION_DAYS + 1) days
    for i in range(DEFAULT_RETENTION_DAYS + 1):
        date = datetime.now() - timedelta(days=i)
        chat_history.add_message(
            user_id,
            f"Message {i}",
            f"Response {i}",
            {"day": i}
        )
    
    # Clean up old history
    chat_history.cleanup_old_history()
    
    # Get today's history
    today = datetime.now().date()
    history = chat_history.get_chat_history(datetime.combine(today, datetime.min.time()))
    
    assert len(history) == 1  # Only today's message should remain

def test_get_statistics(chat_history):
    """Test getting chat history statistics."""
    user_id = "test_user"
    
    # Add multiple messages
    for i in range(5):
        chat_history.add_message(
            user_id,
            f"Message {i}",
            f"Response {i}",
            {"type": "test"}
        )
    
    # Get today's statistics
    today = datetime.now().date()
    stats = chat_history.get_statistics(datetime.combine(today, datetime.min.time()))
    
    assert stats["total_messages"] == 5
    assert stats["unique_users"] == 1
    assert stats["average_messages_per_user"] == 5.0

def test_scheduler_tasks(scheduler):
    """Test scheduler functionality."""
    # Schedule a task
    task_name = "test_task"
    scheduler.schedule_daily_cleanup(hour=0, minute=0)
    
    # Get scheduled tasks
    tasks = scheduler.get_scheduled_tasks()
    
    assert len(tasks) > 0
    assert any(task["name"] == "daily_cleanup" for task in tasks)
    
    # Remove task
    scheduler.remove_task("daily_cleanup")
    tasks = scheduler.get_scheduled_tasks()
    assert not any(task["name"] == "daily_cleanup" for task in tasks)

def test_max_messages_per_file(chat_history):
    """Test handling of maximum messages per file."""
    user_id = "test_user"
    
    # Add more messages than MAX_MESSAGES_PER_FILE
    for i in range(MAX_MESSAGES_PER_FILE + 1):
        chat_history.add_message(
            user_id,
            f"Message {i}",
            f"Response {i}",
            {"index": i}
        )
    
    # Get today's history
    today = datetime.now().date()
    history = chat_history.get_chat_history(datetime.combine(today, datetime.min.time()))
    
    assert len(history) == MAX_MESSAGES_PER_FILE + 1

def test_error_handling(chat_history):
    """Test error handling in chat history operations."""
    # Test with invalid user_id
    with pytest.raises(ValueError):
        chat_history.add_message("", "message", "response")
    
    # Test with invalid date
    with pytest.raises(ValueError):
        chat_history.get_chat_history(None)
    
    # Test with invalid days parameter
    with pytest.raises(ValueError):
        chat_history.get_user_history("test_user", days=-1)

def test_concurrent_access(chat_history):
    """Test concurrent access to chat history."""
    import threading
    
    def add_messages(user_id):
        for i in range(10):
            chat_history.add_message(
                user_id,
                f"Message {i}",
                f"Response {i}",
                {"thread": user_id}
            )
    
    # Create multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=add_messages, args=(f"user_{i}",))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Get today's history
    today = datetime.now().date()
    history = chat_history.get_chat_history(datetime.combine(today, datetime.min.time()))
    
    assert len(history) == 50  # 5 users * 10 messages each 