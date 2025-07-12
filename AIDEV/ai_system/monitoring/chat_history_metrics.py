from prometheus_client import Counter, Histogram, Gauge, Summary
import time
from functools import wraps
from typing import Callable, Any
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Message metrics
messages_total = Counter(
    'chat_messages_total',
    'Total number of chat messages processed',
    ['user_id', 'message_type']
)

message_processing_time = Histogram(
    'chat_message_processing_seconds',
    'Time spent processing chat messages',
    ['operation']
)

# Storage metrics
storage_size = Gauge(
    'chat_history_storage_bytes',
    'Total size of chat history storage in bytes'
)

file_count = Gauge(
    'chat_history_files_total',
    'Total number of chat history files'
)

# User metrics
active_users = Gauge(
    'chat_active_users_total',
    'Number of active users in the last 24 hours'
)

user_messages = Counter(
    'chat_user_messages_total',
    'Total number of messages per user',
    ['user_id']
)

# Performance metrics
response_time = Summary(
    'chat_response_time_seconds',
    'Time spent generating responses'
)

error_count = Counter(
    'chat_errors_total',
    'Total number of errors',
    ['error_type']
)

# Scheduler metrics
scheduled_tasks = Gauge(
    'chat_scheduled_tasks_total',
    'Number of scheduled tasks'
)

task_execution_time = Histogram(
    'chat_task_execution_seconds',
    'Time spent executing scheduled tasks',
    ['task_type']
)

def track_metrics(func: Callable) -> Callable:
    """Decorator to track metrics for functions."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            message_processing_time.labels(operation=func.__name__).observe(
                time.time() - start_time
            )
            return result
        except Exception as e:
            error_count.labels(error_type=type(e).__name__).inc()
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

class ChatHistoryMetrics:
    """Class to manage chat history metrics."""
    
    @staticmethod
    def record_message(user_id: str, message_type: str) -> None:
        """Record a new message."""
        messages_total.labels(user_id=user_id, message_type=message_type).inc()
        user_messages.labels(user_id=user_id).inc()
    
    @staticmethod
    def update_storage_metrics(size_bytes: int, file_count_value: int) -> None:
        """Update storage-related metrics."""
        storage_size.set(size_bytes)
        file_count.set(file_count_value)
    
    @staticmethod
    def update_active_users(count: int) -> None:
        """Update active users count."""
        active_users.set(count)
    
    @staticmethod
    def record_response_time(seconds: float) -> None:
        """Record response generation time."""
        response_time.observe(seconds)
    
    @staticmethod
    def record_task_execution(task_type: str, seconds: float) -> None:
        """Record task execution time."""
        task_execution_time.labels(task_type=task_type).observe(seconds)
    
    @staticmethod
    def update_scheduled_tasks(count: int) -> None:
        """Update scheduled tasks count."""
        scheduled_tasks.set(count)
    
    @staticmethod
    def record_error(error_type: str) -> None:
        """Record an error occurrence."""
        error_count.labels(error_type=error_type).inc()

# Initialize metrics instance
metrics = ChatHistoryMetrics() 