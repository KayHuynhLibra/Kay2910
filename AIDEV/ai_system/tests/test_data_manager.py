import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
from datetime import datetime
import os
import json
from ..data.data_manager import DataManager

@pytest.fixture
def data_manager():
    config = {
        "data_dir": "test_data"
    }
    return DataManager(config)

@pytest.fixture
def sample_dataset():
    return pd.DataFrame({
        'A': [1, 2, 3, np.nan, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': [0.1, 0.2, 0.3, 0.4, 0.5]
    })

def test_setup_logging(data_manager):
    assert data_manager.logger is not None
    assert data_manager.logger.name == "data_manager"
    assert data_manager.logger.level == 20  # INFO level

def test_load_dataset(data_manager, sample_dataset, tmp_path):
    # Save a dataset first
    dataset_name = "test_dataset"
    dataset_path = os.path.join(tmp_path, dataset_name)
    os.makedirs(dataset_path, exist_ok=True)
    
    sample_dataset.to_csv(os.path.join(dataset_path, "latest.csv"), index=False)
    
    # Update config to use tmp_path
    data_manager.config["data_dir"] = str(tmp_path)
    
    # Load dataset
    loaded_dataset = data_manager.load_dataset(dataset_name)
    assert loaded_dataset is not None
    assert dataset_name in data_manager.datasets
    assert dataset_name in data_manager.dataset_versions
    pd.testing.assert_frame_equal(loaded_dataset, sample_dataset)

def test_save_dataset(data_manager, sample_dataset, tmp_path):
    # Update config to use tmp_path
    data_manager.config["data_dir"] = str(tmp_path)
    
    # Save dataset
    dataset_name = "test_dataset"
    data_manager.save_dataset(dataset_name, sample_dataset)
    
    # Verify dataset was saved
    dataset_path = os.path.join(tmp_path, dataset_name, "latest.csv")
    assert os.path.exists(dataset_path)
    assert dataset_name in data_manager.datasets
    assert dataset_name in data_manager.dataset_versions

def test_get_dataset(data_manager, sample_dataset):
    dataset_name = "test_dataset"
    data_manager.datasets[dataset_name] = sample_dataset
    
    # Get existing dataset
    dataset = data_manager.get_dataset(dataset_name)
    assert dataset is not None
    pd.testing.assert_frame_equal(dataset, sample_dataset)
    
    # Get non-existent dataset
    dataset = data_manager.get_dataset("non_existent")
    assert dataset is None

def test_list_datasets(data_manager, sample_dataset):
    # Add some datasets
    data_manager.datasets["dataset1"] = sample_dataset
    data_manager.datasets["dataset2"] = sample_dataset
    
    datasets = data_manager.list_datasets()
    assert len(datasets) == 2
    assert "dataset1" in datasets
    assert "dataset2" in datasets

def test_list_versions(data_manager, tmp_path):
    # Update config to use tmp_path
    data_manager.config["data_dir"] = str(tmp_path)
    
    # Create some versions
    dataset_name = "test_dataset"
    dataset_path = os.path.join(tmp_path, dataset_name)
    os.makedirs(dataset_path, exist_ok=True)
    
    for version in ["v1", "v2", "latest"]:
        pd.DataFrame({'A': [1, 2, 3]}).to_csv(
            os.path.join(dataset_path, f"{version}.csv"),
            index=False
        )
    
    versions = data_manager.list_versions(dataset_name)
    assert len(versions) == 3
    assert "v1" in versions
    assert "v2" in versions
    assert "latest" in versions

def test_delete_dataset(data_manager, sample_dataset, tmp_path):
    # Update config to use tmp_path
    data_manager.config["data_dir"] = str(tmp_path)
    
    # Save a dataset
    dataset_name = "test_dataset"
    data_manager.save_dataset(dataset_name, sample_dataset)
    
    # Delete dataset
    data_manager.delete_dataset(dataset_name)
    
    # Verify dataset was deleted
    assert dataset_name not in data_manager.datasets
    assert dataset_name not in data_manager.dataset_versions
    assert not os.path.exists(os.path.join(tmp_path, dataset_name, "latest.csv"))

def test_preprocess_dataset(data_manager, sample_dataset):
    # Add dataset
    dataset_name = "test_dataset"
    data_manager.datasets[dataset_name] = sample_dataset
    
    # Test preprocessing steps
    preprocessing_config = {
        "steps": [
            {
                "type": "fill_missing",
                "parameters": {"value": 0}
            },
            {
                "type": "normalize",
                "parameters": {"columns": ["A", "C"]}
            }
        ]
    }
    
    processed_dataset = data_manager.preprocess_dataset(dataset_name, preprocessing_config)
    assert processed_dataset is not None
    assert not processed_dataset.isnull().any().any()
    assert abs(processed_dataset["A"].mean()) < 1e-6
    assert abs(processed_dataset["C"].mean()) < 1e-6

def test_split_dataset(data_manager, sample_dataset):
    # Add dataset
    dataset_name = "test_dataset"
    data_manager.datasets[dataset_name] = sample_dataset
    
    # Test splitting
    split_config = {
        "train_ratio": 0.6,
        "val_ratio": 0.2,
        "test_ratio": 0.2,
        "random_state": 42
    }
    
    splits = data_manager.split_dataset(dataset_name, split_config)
    assert "train" in splits
    assert "val" in splits
    assert "test" in splits
    assert len(splits["train"]) == 3
    assert len(splits["val"]) == 1
    assert len(splits["test"]) == 1

def test_update_dataset_metadata(data_manager, sample_dataset, tmp_path):
    # Update config to use tmp_path
    data_manager.config["data_dir"] = str(tmp_path)
    
    # Save a dataset
    dataset_name = "test_dataset"
    data_manager.save_dataset(dataset_name, sample_dataset)
    
    # Verify metadata was created
    metadata_path = os.path.join(tmp_path, dataset_name, "metadata.json")
    assert os.path.exists(metadata_path)
    
    # Check metadata content
    metadata = data_manager.get_dataset_metadata(dataset_name)
    assert "name" in metadata
    assert "version" in metadata
    assert "last_updated" in metadata
    assert "path" in metadata
    assert "shape" in metadata
    assert "columns" in metadata
    assert "dtypes" in metadata
    assert "missing_values" in metadata
    assert "hash" in metadata

def test_save_and_load_state(data_manager, tmp_path):
    # Add some state
    data_manager.datasets["test_dataset"] = pd.DataFrame({'A': [1, 2, 3]})
    data_manager.dataset_versions["test_dataset"] = "latest"
    data_manager.dataset_metadata["test_dataset_latest"] = {
        "name": "test_dataset",
        "version": "latest",
        "last_updated": datetime.now().isoformat(),
        "path": "test/path"
    }
    
    # Save state
    state_file = os.path.join(tmp_path, "data_manager_state.json")
    data_manager.save_state(state_file)
    
    # Create new manager and load state
    new_manager = DataManager({"data_dir": "test_data"})
    new_manager.load_state(state_file)
    
    # Verify state was loaded correctly
    assert "test_dataset" in new_manager.dataset_versions
    assert "test_dataset_latest" in new_manager.dataset_metadata 