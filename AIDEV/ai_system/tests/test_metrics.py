import pytest
import time
from unittest.mock import patch, MagicMock
from ..monitoring.metrics import (
    track_request,
    track_chat,
    track_learning,
    update_system_metrics,
    REQUEST_COUNT,
    REQUEST_LATENCY,
    CHAT_MESSAGE_COUNT,
    CHAT_RESPONSE_TIME,
    MODEL_TRAINING_COUNT,
    MODEL_TRAINING_TIME,
    MEMORY_USAGE,
    CPU_USAGE
)

def test_track_request():
    @track_request
    def test_function():
        time.sleep(0.1)
        return "success"

    result = test_function()
    assert result == "success"
    assert REQUEST_COUNT._value.get() > 0
    assert REQUEST_LATENCY._sum.get() > 0

def test_track_chat():
    @track_chat
    def test_chat(message):
        time.sleep(0.1)
        return f"Response to {message}"

    result = test_chat("test message")
    assert result == "Response to test message"
    assert CHAT_MESSAGE_COUNT._value.get() > 0
    assert CHAT_RESPONSE_TIME._sum.get() > 0

def test_track_learning():
    @track_learning
    def test_training(model_name):
        time.sleep(0.1)
        return f"Trained {model_name}"

    result = test_training("test_model")
    assert result == "Trained test_model"
    assert MODEL_TRAINING_COUNT._value.get() > 0
    assert MODEL_TRAINING_TIME._sum.get() > 0

@patch('psutil.virtual_memory')
@patch('psutil.cpu_percent')
def test_update_system_metrics(mock_cpu, mock_memory):
    mock_memory.return_value = MagicMock(percent=50.0, used=500000000)
    mock_cpu.return_value = 25.0

    update_system_metrics()

    assert MEMORY_USAGE._value.get() == 500000000
    assert CPU_USAGE._value.get() == 25.0

def test_metrics_labels():
    @track_request
    def test_function():
        return "success"

    test_function()
    assert REQUEST_COUNT._value.get() > 0

    @track_chat
    def test_chat(message):
        return f"Response to {message}"

    test_chat("test message")
    assert CHAT_MESSAGE_COUNT._value.get() > 0

    @track_learning
    def test_training(model_name):
        return f"Trained {model_name}"

    test_training("test_model")
    assert MODEL_TRAINING_COUNT._value.get() > 0

def test_metrics_error_handling():
    @track_request
    def test_error_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_error_function()

    assert REQUEST_COUNT._value.get() > 0
    assert REQUEST_LATENCY._sum.get() > 0

@patch('psutil.virtual_memory')
@patch('psutil.cpu_percent')
def test_system_metrics_error_handling(mock_cpu, mock_memory):
    mock_memory.side_effect = Exception("Memory error")
    mock_cpu.side_effect = Exception("CPU error")

    # Should not raise exception
    update_system_metrics() 