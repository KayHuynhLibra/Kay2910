import pytest
import numpy as np
from unittest.mock import Mock, patch
from datetime import datetime
import os
import pickle
from ..models.model_manager import ModelManager

@pytest.fixture
def model_manager():
    config = {
        "model_dir": "test_models"
    }
    return ModelManager(config)

@pytest.fixture
def sample_model():
    class DummyModel:
        def __init__(self):
            self.weights = np.random.rand(10)
            
        def predict(self, X):
            return np.random.rand(len(X))
            
    return DummyModel()

def test_setup_logging(model_manager):
    assert model_manager.logger is not None
    assert model_manager.logger.name == "model_manager"
    assert model_manager.logger.level == 20  # INFO level

def test_load_model(model_manager, sample_model, tmp_path):
    # Save a model first
    model_name = "test_model"
    model_path = os.path.join(tmp_path, model_name)
    os.makedirs(model_path, exist_ok=True)
    
    with open(os.path.join(model_path, "latest.pkl"), "wb") as f:
        pickle.dump(sample_model, f)
    
    # Update config to use tmp_path
    model_manager.config["model_dir"] = str(tmp_path)
    
    # Load model
    loaded_model = model_manager.load_model(model_name)
    assert loaded_model is not None
    assert model_name in model_manager.models
    assert model_name in model_manager.model_versions

def test_save_model(model_manager, sample_model, tmp_path):
    # Update config to use tmp_path
    model_manager.config["model_dir"] = str(tmp_path)
    
    # Save model
    model_name = "test_model"
    model_manager.save_model(model_name, sample_model)
    
    # Verify model was saved
    model_path = os.path.join(tmp_path, model_name, "latest.pkl")
    assert os.path.exists(model_path)
    assert model_name in model_manager.models
    assert model_name in model_manager.model_versions

def test_get_model(model_manager, sample_model):
    model_name = "test_model"
    model_manager.models[model_name] = sample_model
    
    # Get existing model
    model = model_manager.get_model(model_name)
    assert model is not None
    assert model == sample_model
    
    # Get non-existent model
    model = model_manager.get_model("non_existent")
    assert model is None

def test_list_models(model_manager, sample_model):
    # Add some models
    model_manager.models["model1"] = sample_model
    model_manager.models["model2"] = sample_model
    
    models = model_manager.list_models()
    assert len(models) == 2
    assert "model1" in models
    assert "model2" in models

def test_list_versions(model_manager, tmp_path):
    # Update config to use tmp_path
    model_manager.config["model_dir"] = str(tmp_path)
    
    # Create some versions
    model_name = "test_model"
    model_path = os.path.join(tmp_path, model_name)
    os.makedirs(model_path, exist_ok=True)
    
    for version in ["v1", "v2", "latest"]:
        with open(os.path.join(model_path, f"{version}.pkl"), "wb") as f:
            pickle.dump(Mock(), f)
    
    versions = model_manager.list_versions(model_name)
    assert len(versions) == 3
    assert "v1" in versions
    assert "v2" in versions
    assert "latest" in versions

def test_delete_model(model_manager, sample_model, tmp_path):
    # Update config to use tmp_path
    model_manager.config["model_dir"] = str(tmp_path)
    
    # Save a model
    model_name = "test_model"
    model_manager.save_model(model_name, sample_model)
    
    # Delete model
    model_manager.delete_model(model_name)
    
    # Verify model was deleted
    assert model_name not in model_manager.models
    assert model_name not in model_manager.model_versions
    assert not os.path.exists(os.path.join(tmp_path, model_name, "latest.pkl"))

def test_update_model_metadata(model_manager, sample_model, tmp_path):
    # Update config to use tmp_path
    model_manager.config["model_dir"] = str(tmp_path)
    
    # Save a model
    model_name = "test_model"
    model_manager.save_model(model_name, sample_model)
    
    # Verify metadata was created
    metadata_path = os.path.join(tmp_path, model_name, "metadata.json")
    assert os.path.exists(metadata_path)
    
    # Check metadata content
    metadata = model_manager.get_model_metadata(model_name)
    assert "name" in metadata
    assert "version" in metadata
    assert "last_updated" in metadata
    assert "path" in metadata

def test_save_and_load_state(model_manager, tmp_path):
    # Add some state
    model_manager.models["test_model"] = Mock()
    model_manager.model_versions["test_model"] = "latest"
    model_manager.model_metadata["test_model_latest"] = {
        "name": "test_model",
        "version": "latest",
        "last_updated": datetime.now().isoformat(),
        "path": "test/path"
    }
    
    # Save state
    state_file = os.path.join(tmp_path, "model_manager_state.json")
    model_manager.save_state(state_file)
    
    # Create new manager and load state
    new_manager = ModelManager({"model_dir": "test_models"})
    new_manager.load_state(state_file)
    
    # Verify state was loaded correctly
    assert "test_model" in new_manager.model_versions
    assert "test_model_latest" in new_manager.model_metadata 