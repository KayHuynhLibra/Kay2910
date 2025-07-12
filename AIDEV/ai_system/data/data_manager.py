from typing import Any, Dict, List, Optional, Union
import os
import json
import pandas as pd
import numpy as np
from datetime import datetime
import logging
import hashlib
from pathlib import Path

class DataManager:
    """
    Manager for handling data operations including loading, saving,
    preprocessing, and versioning of datasets.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the data manager.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary
        """
        self.config = config
        self.datasets = {}
        self.dataset_versions = {}
        self.dataset_metadata = {}
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """
        Setup logging configuration.
        
        Returns:
            logging.Logger: Configured logger
        """
        logger = logging.getLogger("data_manager")
        logger.setLevel(logging.INFO)
        
        # Create handlers
        file_handler = logging.FileHandler("logs/data_manager.log")
        console_handler = logging.StreamHandler()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
        
    def load_dataset(self, dataset_name: str, version: Optional[str] = None) -> pd.DataFrame:
        """
        Load a dataset from disk.
        
        Args:
            dataset_name (str): Name of the dataset
            version (Optional[str]): Version of the dataset to load
            
        Returns:
            pd.DataFrame: Loaded dataset
        """
        try:
            dataset_path = self._get_dataset_path(dataset_name, version)
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset not found at {dataset_path}")
                
            # Load dataset based on file extension
            if dataset_path.endswith('.csv'):
                dataset = pd.read_csv(dataset_path)
            elif dataset_path.endswith('.json'):
                dataset = pd.read_json(dataset_path)
            elif dataset_path.endswith('.parquet'):
                dataset = pd.read_parquet(dataset_path)
            else:
                raise ValueError(f"Unsupported file format: {dataset_path}")
                
            # Update dataset registry
            self.datasets[dataset_name] = dataset
            self.dataset_versions[dataset_name] = version or "latest"
            
            self.logger.info(f"Dataset {dataset_name} loaded successfully")
            return dataset
            
        except Exception as e:
            self.logger.error(f"Error loading dataset: {str(e)}")
            raise
            
    def save_dataset(self, dataset_name: str, dataset: pd.DataFrame, version: Optional[str] = None) -> None:
        """
        Save a dataset to disk.
        
        Args:
            dataset_name (str): Name of the dataset
            dataset (pd.DataFrame): Dataset to save
            version (Optional[str]): Version to save as
        """
        try:
            dataset_path = self._get_dataset_path(dataset_name, version)
            os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
            
            # Save dataset based on file extension
            if dataset_path.endswith('.csv'):
                dataset.to_csv(dataset_path, index=False)
            elif dataset_path.endswith('.json'):
                dataset.to_json(dataset_path, orient='records')
            elif dataset_path.endswith('.parquet'):
                dataset.to_parquet(dataset_path, index=False)
            else:
                raise ValueError(f"Unsupported file format: {dataset_path}")
                
            # Update dataset registry
            self.datasets[dataset_name] = dataset
            self.dataset_versions[dataset_name] = version or "latest"
            
            # Update metadata
            self._update_dataset_metadata(dataset_name, version, dataset)
            
            self.logger.info(f"Dataset {dataset_name} saved successfully")
            
        except Exception as e:
            self.logger.error(f"Error saving dataset: {str(e)}")
            raise
            
    def get_dataset(self, dataset_name: str) -> Optional[pd.DataFrame]:
        """
        Get a loaded dataset.
        
        Args:
            dataset_name (str): Name of the dataset
            
        Returns:
            Optional[pd.DataFrame]: Dataset if loaded, None otherwise
        """
        return self.datasets.get(dataset_name)
        
    def list_datasets(self) -> List[str]:
        """
        List all available datasets.
        
        Returns:
            List[str]: List of dataset names
        """
        return list(self.datasets.keys())
        
    def list_versions(self, dataset_name: str) -> List[str]:
        """
        List all versions of a dataset.
        
        Args:
            dataset_name (str): Name of the dataset
            
        Returns:
            List[str]: List of version strings
        """
        dataset_dir = os.path.join(self.config["data_dir"], dataset_name)
        if not os.path.exists(dataset_dir):
            return []
            
        versions = []
        for file in os.listdir(dataset_dir):
            if file.endswith(('.csv', '.json', '.parquet')):
                versions.append(file.split('.')[0])
        return versions
        
    def delete_dataset(self, dataset_name: str, version: Optional[str] = None) -> None:
        """
        Delete a dataset.
        
        Args:
            dataset_name (str): Name of the dataset
            version (Optional[str]): Version to delete
        """
        try:
            dataset_path = self._get_dataset_path(dataset_name, version)
            if os.path.exists(dataset_path):
                os.remove(dataset_path)
                
            # Update registry
            if version == self.dataset_versions.get(dataset_name):
                del self.datasets[dataset_name]
                del self.dataset_versions[dataset_name]
                
            self.logger.info(f"Dataset {dataset_name} deleted successfully")
            
        except Exception as e:
            self.logger.error(f"Error deleting dataset: {str(e)}")
            raise
            
    def preprocess_dataset(self, dataset_name: str, preprocessing_config: Dict[str, Any]) -> pd.DataFrame:
        """
        Preprocess a dataset according to configuration.
        
        Args:
            dataset_name (str): Name of the dataset
            preprocessing_config (Dict[str, Any]): Preprocessing configuration
            
        Returns:
            pd.DataFrame: Preprocessed dataset
        """
        try:
            dataset = self.get_dataset(dataset_name)
            if dataset is None:
                raise ValueError(f"Dataset {dataset_name} not found")
                
            # Apply preprocessing steps
            for step in preprocessing_config.get("steps", []):
                step_type = step.get("type")
                params = step.get("parameters", {})
                
                if step_type == "drop_columns":
                    dataset = dataset.drop(columns=params.get("columns", []))
                elif step_type == "fill_missing":
                    dataset = dataset.fillna(params.get("value", 0))
                elif step_type == "normalize":
                    columns = params.get("columns", dataset.columns)
                    dataset[columns] = (dataset[columns] - dataset[columns].mean()) / dataset[columns].std()
                elif step_type == "encode_categorical":
                    columns = params.get("columns", [])
                    dataset = pd.get_dummies(dataset, columns=columns)
                else:
                    self.logger.warning(f"Unknown preprocessing step: {step_type}")
                    
            return dataset
            
        except Exception as e:
            self.logger.error(f"Error preprocessing dataset: {str(e)}")
            raise
            
    def split_dataset(self, dataset_name: str, split_config: Dict[str, Any]) -> Dict[str, pd.DataFrame]:
        """
        Split a dataset into train, validation, and test sets.
        
        Args:
            dataset_name (str): Name of the dataset
            split_config (Dict[str, Any]): Split configuration
            
        Returns:
            Dict[str, pd.DataFrame]: Dictionary of split datasets
        """
        try:
            dataset = self.get_dataset(dataset_name)
            if dataset is None:
                raise ValueError(f"Dataset {dataset_name} not found")
                
            # Get split ratios
            train_ratio = split_config.get("train_ratio", 0.7)
            val_ratio = split_config.get("val_ratio", 0.15)
            test_ratio = split_config.get("test_ratio", 0.15)
            
            # Validate ratios
            if abs(train_ratio + val_ratio + test_ratio - 1.0) > 1e-6:
                raise ValueError("Split ratios must sum to 1.0")
                
            # Shuffle dataset
            dataset = dataset.sample(frac=1, random_state=split_config.get("random_state", 42))
            
            # Calculate split indices
            n = len(dataset)
            train_end = int(n * train_ratio)
            val_end = train_end + int(n * val_ratio)
            
            # Split dataset
            splits = {
                "train": dataset[:train_end],
                "val": dataset[train_end:val_end],
                "test": dataset[val_end:]
            }
            
            return splits
            
        except Exception as e:
            self.logger.error(f"Error splitting dataset: {str(e)}")
            raise
            
    def _get_dataset_path(self, dataset_name: str, version: Optional[str] = None) -> str:
        """
        Get the path for a dataset file.
        
        Args:
            dataset_name (str): Name of the dataset
            version (Optional[str]): Version of the dataset
            
        Returns:
            str: Path to dataset file
        """
        version = version or "latest"
        return os.path.join(
            self.config["data_dir"],
            dataset_name,
            f"{version}.csv"  # Default to CSV format
        )
        
    def _update_dataset_metadata(self, dataset_name: str, version: Optional[str], dataset: pd.DataFrame) -> None:
        """
        Update dataset metadata.
        
        Args:
            dataset_name (str): Name of the dataset
            version (Optional[str]): Version of the dataset
            dataset (pd.DataFrame): Dataset
        """
        metadata = {
            "name": dataset_name,
            "version": version or "latest",
            "last_updated": datetime.now().isoformat(),
            "path": self._get_dataset_path(dataset_name, version),
            "shape": dataset.shape,
            "columns": dataset.columns.tolist(),
            "dtypes": dataset.dtypes.astype(str).to_dict(),
            "missing_values": dataset.isnull().sum().to_dict(),
            "hash": self._compute_dataset_hash(dataset)
        }
        
        self.dataset_metadata[f"{dataset_name}_{version}"] = metadata
        
        # Save metadata to file
        metadata_path = os.path.join(
            self.config["data_dir"],
            dataset_name,
            "metadata.json"
        )
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
            
    def _compute_dataset_hash(self, dataset: pd.DataFrame) -> str:
        """
        Compute hash of dataset for versioning.
        
        Args:
            dataset (pd.DataFrame): Dataset
            
        Returns:
            str: Hash string
        """
        # Convert dataset to bytes
        dataset_bytes = dataset.to_csv(index=False).encode()
        
        # Compute hash
        return hashlib.sha256(dataset_bytes).hexdigest()
        
    def get_dataset_metadata(self, dataset_name: str, version: Optional[str] = None) -> Dict[str, Any]:
        """
        Get metadata for a dataset.
        
        Args:
            dataset_name (str): Name of the dataset
            version (Optional[str]): Version of the dataset
            
        Returns:
            Dict[str, Any]: Dataset metadata
        """
        version = version or "latest"
        return self.dataset_metadata.get(f"{dataset_name}_{version}", {})
        
    def save_state(self, filepath: str) -> None:
        """
        Save manager state to file.
        
        Args:
            filepath (str): Path to save state
        """
        try:
            state = {
                "config": self.config,
                "dataset_versions": self.dataset_versions,
                "dataset_metadata": self.dataset_metadata
            }
            with open(filepath, 'w') as f:
                json.dump(state, f)
            self.logger.info(f"State saved to {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving state: {str(e)}")
            
    def load_state(self, filepath: str) -> None:
        """
        Load manager state from file.
        
        Args:
            filepath (str): Path to load state from
        """
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            self.config = state["config"]
            self.dataset_versions = state["dataset_versions"]
            self.dataset_metadata = state["dataset_metadata"]
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}") 