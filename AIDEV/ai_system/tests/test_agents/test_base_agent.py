import pytest
import os
import json
from datetime import datetime
from agents.base_agent import BaseAgent

class TestAgent(BaseAgent):
    """Test implementation of BaseAgent for testing purposes."""
    
    async def process(self, input_data):
        return {"result": "test"}
        
    async def learn(self, data):
        self.memory["test"] = data

@pytest.fixture
def test_config():
    return {
        "required_fields": ["test_field"],
        "cache_ttl": 3600
    }

@pytest.fixture
def test_agent(test_config):
    return TestAgent("test", test_config)

def test_agent_initialization(test_agent, test_config):
    """Test agent initialization."""
    assert test_agent.name == "test"
    assert test_agent.config == test_config
    assert isinstance(test_agent.memory, dict)
    assert isinstance(test_agent.cache, dict)
    
def test_input_validation(test_agent):
    """Test input validation."""
    # Test valid input
    valid_input = {"test_field": "value"}
    assert test_agent._validate_input(valid_input) is True
    
    # Test invalid input
    invalid_input = {"wrong_field": "value"}
    assert test_agent._validate_input(invalid_input) is False
    
def test_caching(test_agent):
    """Test caching functionality."""
    # Test caching result
    test_agent._cache_result("test_key", "test_value")
    assert "test_key" in test_agent.cache
    
    # Test retrieving cached result
    cached_result = test_agent._get_cached_result("test_key")
    assert cached_result == "test_value"
    
    # Test cache expiration
    test_agent.cache["test_key"]["timestamp"] = datetime.now().timestamp() - 3601
    expired_result = test_agent._get_cached_result("test_key")
    assert expired_result is None
    
def test_state_management(test_agent, tmp_path):
    """Test state saving and loading."""
    # Save state
    state_file = tmp_path / "test_state.json"
    test_agent.save_state(str(state_file))
    assert state_file.exists()
    
    # Load state
    new_agent = TestAgent("new_test", {})
    new_agent.load_state(str(state_file))
    assert new_agent.name == "test"
    assert new_agent.config == test_agent.config
    
def test_memory_management(test_agent):
    """Test memory management."""
    # Test adding to memory
    test_data = {"test": "data"}
    test_agent.memory["test_key"] = test_data
    assert test_agent.memory["test_key"] == test_data
    
    # Test clearing memory
    test_agent.clear_memory()
    assert test_agent.memory == {}
    
def test_cache_management(test_agent):
    """Test cache management."""
    # Test adding to cache
    test_agent._cache_result("test_key", "test_value")
    assert "test_key" in test_agent.cache
    
    # Test clearing cache
    test_agent.clear_cache()
    assert test_agent.cache == {}
    
@pytest.mark.asyncio
async def test_process_method(test_agent):
    """Test process method."""
    result = await test_agent.process({"test_field": "value"})
    assert result == {"result": "test"}
    
@pytest.mark.asyncio
async def test_learn_method(test_agent):
    """Test learn method."""
    test_data = {"test": "data"}
    await test_agent.learn(test_data)
    assert test_agent.memory["test"] == test_data 