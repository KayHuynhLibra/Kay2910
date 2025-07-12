import pytest
import numpy as np
from mcb_example import Context, SimpleModel, SimpleBehavior, MCBSystem

def test_simple_model():
    model = SimpleModel()
    input_data = np.random.randn(10)
    
    # Test prediction
    output = model.predict(input_data)
    assert isinstance(output, float)
    
    # Test update
    original_weights = model.weights.copy()
    model.update(input_data)
    assert not np.array_equal(original_weights, model.weights)

def test_simple_behavior():
    behavior = SimpleBehavior()
    context = Context(
        environment={"temperature": 25, "humidity": 60},
        user_profile={},
        system_state={}
    )
    
    # Test validation
    assert behavior.validate(context)
    
    # Test execution
    result = behavior.execute(context, 0.7)
    assert result["action"] == "recommend"
    assert result["confidence"] == 0.7
    assert "temperature" in result["context_used"]

def test_mcb_system():
    model = SimpleModel()
    behavior = SimpleBehavior()
    system = MCBSystem(model, behavior)
    
    input_data = np.random.randn(10)
    context = Context(
        environment={"temperature": 25, "humidity": 60},
        user_profile={},
        system_state={}
    )
    
    # Test processing
    result = system.process(input_data, context)
    assert isinstance(result, dict)
    assert "action" in result
    assert "confidence" in result
    assert "context_used" in result
    
    # Test context history
    assert len(system.context_history) == 1
    assert system.context_history[0] == context

def test_invalid_context():
    model = SimpleModel()
    behavior = SimpleBehavior()
    system = MCBSystem(model, behavior)
    
    input_data = np.random.randn(10)
    invalid_context = Context(
        environment={},  # Missing required fields
        user_profile={},
        system_state={}
    )
    
    # Test error handling
    with pytest.raises(ValueError):
        system.process(input_data, invalid_context) 