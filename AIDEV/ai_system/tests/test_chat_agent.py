import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from ..agents.chat_agent import ChatAgent

@pytest.fixture
def chat_agent():
    config = {
        "openai_api_key": "test_key",
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 150,
        "max_history": 100,
        "response_templates": {
            "hello": "Hi there!",
            "bye": "Goodbye!"
        }
    }
    return ChatAgent("test_chat_agent", config)

@pytest.mark.asyncio
async def test_process_valid_input(chat_agent):
    input_data = {
        "message": "hello",
        "context": {"user_id": "123"}
    }
    result = await chat_agent.process(input_data)
    assert "response" in result
    assert "context" in result
    assert "timestamp" in result
    assert result["context"]["user_id"] == "123"

@pytest.mark.asyncio
async def test_process_invalid_input(chat_agent):
    input_data = {}
    result = await chat_agent.process(input_data)
    assert "error" in result
    assert result["error"] == "Invalid input data"

@pytest.mark.asyncio
async def test_learn(chat_agent):
    data = {
        "patterns": ["test_pattern"],
        "responses": ["test_response"]
    }
    await chat_agent.learn(data)
    assert "test_pattern" in chat_agent.response_templates
    assert chat_agent.response_templates["test_pattern"] == "test_response"

def test_update_context(chat_agent):
    new_context = {"key": "value"}
    chat_agent._update_context(new_context)
    assert chat_agent.context["key"] == "value"

def test_update_history(chat_agent):
    message = "test message"
    response = "test response"
    chat_agent._update_history(message, response)
    assert len(chat_agent.conversation_history) == 1
    assert chat_agent.conversation_history[0]["message"] == message
    assert chat_agent.conversation_history[0]["response"] == response

def test_get_conversation_history(chat_agent):
    # Add some history
    for i in range(5):
        chat_agent._update_history(f"message_{i}", f"response_{i}")
    
    # Test without limit
    history = chat_agent.get_conversation_history()
    assert len(history) == 5
    
    # Test with limit
    limited_history = chat_agent.get_conversation_history(limit=3)
    assert len(limited_history) == 3

def test_clear_history(chat_agent):
    # Add some history
    chat_agent._update_history("test", "test")
    assert len(chat_agent.conversation_history) > 0
    
    # Clear history
    chat_agent.clear_history()
    assert len(chat_agent.conversation_history) == 0

def test_save_and_load_state(chat_agent, tmp_path):
    # Add some state
    chat_agent._update_history("test", "test")
    chat_agent._update_context({"test": "value"})
    
    # Save state
    state_file = tmp_path / "chat_agent_state.json"
    chat_agent.save_state(str(state_file))
    
    # Create new agent and load state
    new_agent = ChatAgent("new_agent", chat_agent.config)
    new_agent.load_state(str(state_file))
    
    # Verify state was loaded correctly
    assert len(new_agent.conversation_history) == 1
    assert new_agent.context["test"] == "value"
    assert new_agent.response_templates == chat_agent.response_templates

@pytest.mark.asyncio
async def test_process_message_with_cache(chat_agent):
    message = "test message"
    
    # First call should process message
    with patch.object(chat_agent, '_generate_response') as mock_generate:
        mock_generate.return_value = "cached response"
        result1 = await chat_agent._process_message(message)
        assert mock_generate.call_count == 1
    
    # Second call should use cache
    with patch.object(chat_agent, '_generate_response') as mock_generate:
        result2 = await chat_agent._process_message(message)
        assert mock_generate.call_count == 0
        assert result1 == result2

def test_generate_response_with_templates(chat_agent):
    # Test with matching template
    response = chat_agent._generate_response("hello")
    assert response == "Hi there!"
    
    # Test with non-matching message
    response = chat_agent._generate_response("unknown message")
    assert response == "I'm not sure how to respond to that." 