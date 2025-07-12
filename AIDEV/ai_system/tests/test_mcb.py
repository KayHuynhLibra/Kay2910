import pytest
import numpy as np
from datetime import datetime
from ai_system.core.mcb import Context, Model, Behavior, MCBSystem

class TestModel(Model):
    def __init__(self):
        self.weights = np.random.randn(10)
        self.metadata = {
            "name": "TestModel",
            "version": "1.0",
            "type": "regression"
        }
    
    def predict(self, input_data: np.ndarray) -> float:
        return np.dot(input_data, self.weights)
    
    def update(self, new_data: np.ndarray) -> None:
        self.weights += 0.01 * new_data
    
    def get_metadata(self) -> dict:
        return self.metadata

class TestBehavior(Behavior):
    def __init__(self):
        self.constraints = {
            "min_temperature": 0,
            "max_temperature": 100,
            "required_fields": ["temperature", "humidity"]
        }
    
    def execute(self, context: Context, model_output: float) -> dict:
        return {
            "action": "recommend" if model_output > 0.5 else "reject",
            "confidence": abs(model_output),
            "context_used": context.environment
        }
    
    def validate(self, context: Context) -> bool:
        return all(key in context.environment for key in self.constraints["required_fields"])
    
    def get_constraints(self) -> dict:
        return self.constraints

def test_mcb_system_initialization():
    model = TestModel()
    behavior = TestBehavior()
    system = MCBSystem(model, behavior)
    
    assert system.model == model
    assert system.behavior == behavior
    assert len(system.context_history) == 0
    assert len(system.execution_history) == 0

def test_mcb_system_processing():
    model = TestModel()
    behavior = TestBehavior()
    system = MCBSystem(model, behavior)
    
    input_data = np.random.randn(10)
    context = Context(
        environment={"temperature": 25, "humidity": 60},
        user_profile={"age": 30},
        system_state={"mode": "normal"}
    )
    
    result = system.process(input_data, context)
    
    assert isinstance(result, dict)
    assert "action" in result
    assert "confidence" in result
    assert "context_used" in result
    assert len(system.context_history) == 1
    assert len(system.execution_history) == 1

def test_mcb_system_invalid_context():
    model = TestModel()
    behavior = TestBehavior()
    system = MCBSystem(model, behavior)
    
    input_data = np.random.randn(10)
    invalid_context = Context(
        environment={},  # Missing required fields
        user_profile={},
        system_state={}
    )
    
    with pytest.raises(ValueError):
        system.process(input_data, invalid_context)

def test_mcb_system_state():
    model = TestModel()
    behavior = TestBehavior()
    system = MCBSystem(model, behavior)
    
    state = system.get_system_state()
    
    assert isinstance(state, dict)
    assert "context_history_size" in state
    assert "execution_history_size" in state
    assert "model_metadata" in state
    assert "behavior_constraints" in state

def test_mcb_system_performance():
    model = TestModel()
    behavior = TestBehavior()
    system = MCBSystem(model, behavior)
    
    # Process some data
    for _ in range(5):
        input_data = np.random.randn(10)
        context = Context(
            environment={"temperature": 25, "humidity": 60},
            user_profile={},
            system_state={}
        )
        system.process(input_data, context)
    
    performance = system.analyze_performance()
    
    assert isinstance(performance, dict)
    assert "total_executions" in performance
    assert "successful_executions" in performance
    assert "success_rate" in performance
    assert "average_response_time" in performance
    assert "context_diversity" in performance
    assert performance["total_executions"] == 5 