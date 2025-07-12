import pytest
import numpy as np
from unittest.mock import Mock, patch
from datetime import datetime
from ..agents.learning_agent import LearningAgent

@pytest.fixture
def learning_agent():
    config = {
        "max_training_history": 100,
        "models": {
            "test_model": {
                "type": "neural_network",
                "parameters": {
                    "hidden_layer_sizes": (10,),
                    "max_iter": 100
                }
            }
        }
    }
    return LearningAgent("test_learning_agent", config)

@pytest.fixture
def sample_data():
    return {
        "features": np.random.rand(100, 10),
        "labels": np.random.randint(0, 2, 100),
        "parameters": {
            "learning_rate": 0.01,
            "batch_size": 32
        }
    }

@pytest.mark.asyncio
async def test_process_train(learning_agent, sample_data):
    input_data = {
        "action": "train",
        "model_name": "test_model",
        "data": sample_data
    }
    result = await learning_agent.process(input_data)
    assert "action" in result
    assert "model_name" in result
    assert "result" in result
    assert "timestamp" in result
    assert result["action"] == "train"

@pytest.mark.asyncio
async def test_process_evaluate(learning_agent, sample_data):
    # First train the model
    await learning_agent.process({
        "action": "train",
        "model_name": "test_model",
        "data": sample_data
    })
    
    # Then evaluate
    input_data = {
        "action": "evaluate",
        "model_name": "test_model",
        "data": sample_data
    }
    result = await learning_agent.process(input_data)
    assert "action" in result
    assert "model_name" in result
    assert "result" in result
    assert "timestamp" in result
    assert result["action"] == "evaluate"

@pytest.mark.asyncio
async def test_process_predict(learning_agent, sample_data):
    # First train the model
    await learning_agent.process({
        "action": "train",
        "model_name": "test_model",
        "data": sample_data
    })
    
    # Then predict
    input_data = {
        "action": "predict",
        "model_name": "test_model",
        "data": {"features": sample_data["features"][:5]}
    }
    result = await learning_agent.process(input_data)
    assert "action" in result
    assert "model_name" in result
    assert "result" in result
    assert "timestamp" in result
    assert result["action"] == "predict"

@pytest.mark.asyncio
async def test_process_invalid_action(learning_agent):
    input_data = {
        "action": "invalid_action",
        "model_name": "test_model",
        "data": {}
    }
    result = await learning_agent.process(input_data)
    assert "error" in result
    assert "Unknown action" in result["error"]

@pytest.mark.asyncio
async def test_learn(learning_agent, sample_data):
    data = {
        "model_name": "test_model",
        "training_data": sample_data,
        "parameters": {"learning_rate": 0.01}
    }
    await learning_agent.learn(data)
    assert f"model_test_model" in learning_agent.memory
    assert "parameters" in learning_agent.memory[f"model_test_model"]

def test_get_or_create_model(learning_agent):
    model = learning_agent._get_or_create_model("test_model")
    assert model is not None
    assert "test_model" in learning_agent.models

def test_get_model(learning_agent):
    # Create model first
    learning_agent._get_or_create_model("test_model")
    
    # Get existing model
    model = learning_agent._get_model("test_model")
    assert model is not None
    
    # Get non-existent model
    model = learning_agent._get_model("non_existent")
    assert model is None

def test_update_training_history(learning_agent):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "parameters": {"learning_rate": 0.01},
        "metrics": {"accuracy": 0.95}
    }
    learning_agent._update_training_history("test_model", entry)
    assert "test_model" in learning_agent.training_history
    assert len(learning_agent.training_history["test_model"]) == 1

def test_get_training_history(learning_agent):
    # Add some history
    for i in range(5):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "parameters": {"learning_rate": 0.01},
            "metrics": {"accuracy": 0.95}
        }
        learning_agent._update_training_history("test_model", entry)
    
    # Test without limit
    history = learning_agent.get_training_history("test_model")
    assert len(history) == 5
    
    # Test with limit
    limited_history = learning_agent.get_training_history("test_model", limit=3)
    assert len(limited_history) == 3

def test_get_evaluation_metrics(learning_agent):
    metrics = {
        "accuracy": 0.95,
        "precision": 0.92,
        "recall": 0.88
    }
    learning_agent.evaluation_metrics["test_model"] = {
        "timestamp": datetime.now().isoformat(),
        "metrics": metrics
    }
    
    result = learning_agent.get_evaluation_metrics("test_model")
    assert "timestamp" in result
    assert "metrics" in result
    assert result["metrics"] == metrics

def test_save_and_load_state(learning_agent, tmp_path):
    # Add some state
    learning_agent._get_or_create_model("test_model")
    learning_agent.evaluation_metrics["test_model"] = {
        "timestamp": datetime.now().isoformat(),
        "metrics": {"accuracy": 0.95}
    }
    
    # Save state
    state_file = tmp_path / "learning_agent_state.json"
    learning_agent.save_state(str(state_file))
    
    # Create new agent and load state
    new_agent = LearningAgent("new_agent", learning_agent.config)
    new_agent.load_state(str(state_file))
    
    # Verify state was loaded correctly
    assert "test_model" in new_agent.models
    assert "test_model" in new_agent.evaluation_metrics 