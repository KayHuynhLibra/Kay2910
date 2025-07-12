from typing import Any, Dict, List, Optional
import os
import json
import pickle
from datetime import datetime
import logging

class ModelManager:
    """
    Manager for handling model operations including loading, saving,
    and managing model versions.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the model manager.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary
        """
        self.config = config
        self.models = {}
        self.model_versions = {}
        self.model_metadata = {}
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """
        Setup logging configuration.
        
        Returns:
            logging.Logger: Configured logger
        """
        logger = logging.getLogger("model_manager")
        logger.setLevel(logging.INFO)
        
        # Create handlers
        file_handler = logging.FileHandler("logs/model_manager.log")
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
        
    def load_model(self, model_name: str, version: Optional[str] = None) -> Any:
        """
        Load a model from disk.
        
        Args:
            model_name (str): Name of the model
            version (Optional[str]): Version of the model to load
            
        Returns:
            Any: Loaded model
        """
        try:
            model_path = self._get_model_path(model_name, version)
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found at {model_path}")
                
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
                
            # Update model registry
            self.models[model_name] = model
            self.model_versions[model_name] = version or "latest"
            
            self.logger.info(f"Model {model_name} loaded successfully")
            return model
            
        except Exception as e:
            self.logger.error(f"Error loading model: {str(e)}")
            raise
            
    def save_model(self, model_name: str, model: Any, version: Optional[str] = None) -> None:
        """
        Save a model to disk.
        
        Args:
            model_name (str): Name of the model
            model (Any): Model to save
            version (Optional[str]): Version to save as
        """
        try:
            model_path = self._get_model_path(model_name, version)
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            
            with open(model_path, 'wb') as f:
                pickle.dump(model, f)
                
            # Update model registry
            self.models[model_name] = model
            self.model_versions[model_name] = version or "latest"
            
            # Update metadata
            self._update_model_metadata(model_name, version)
            
            self.logger.info(f"Model {model_name} saved successfully")
            
        except Exception as e:
            self.logger.error(f"Error saving model: {str(e)}")
            raise
            
    def get_model(self, model_name: str) -> Optional[Any]:
        """
        Get a loaded model.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            Optional[Any]: Model if loaded, None otherwise
        """
        return self.models.get(model_name)
        
    def list_models(self) -> List[str]:
        """
        List all available models.
        
        Returns:
            List[str]: List of model names
        """
        return list(self.models.keys())
        
    def list_versions(self, model_name: str) -> List[str]:
        """
        List all versions of a model.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            List[str]: List of version strings
        """
        model_dir = os.path.join(self.config["model_dir"], model_name)
        if not os.path.exists(model_dir):
            return []
            
        versions = []
        for file in os.listdir(model_dir):
            if file.endswith(".pkl"):
                versions.append(file[:-4])
        return versions
        
    def delete_model(self, model_name: str, version: Optional[str] = None) -> None:
        """
        Delete a model.
        
        Args:
            model_name (str): Name of the model
            version (Optional[str]): Version to delete
        """
        try:
            model_path = self._get_model_path(model_name, version)
            if os.path.exists(model_path):
                os.remove(model_path)
                
            # Update registry
            if version == self.model_versions.get(model_name):
                del self.models[model_name]
                del self.model_versions[model_name]
                
            self.logger.info(f"Model {model_name} deleted successfully")
            
        except Exception as e:
            self.logger.error(f"Error deleting model: {str(e)}")
            raise
            
    def _get_model_path(self, model_name: str, version: Optional[str] = None) -> str:
        """
        Get the path for a model file.
        
        Args:
            model_name (str): Name of the model
            version (Optional[str]): Version of the model
            
        Returns:
            str: Path to model file
        """
        version = version or "latest"
        return os.path.join(
            self.config["model_dir"],
            model_name,
            f"{version}.pkl"
        )
        
    def _update_model_metadata(self, model_name: str, version: Optional[str] = None) -> None:
        """
        Update model metadata.
        
        Args:
            model_name (str): Name of the model
            version (Optional[str]): Version of the model
        """
        metadata = {
            "name": model_name,
            "version": version or "latest",
            "last_updated": datetime.now().isoformat(),
            "path": self._get_model_path(model_name, version)
        }
        
        self.model_metadata[f"{model_name}_{version}"] = metadata
        
        # Save metadata to file
        metadata_path = os.path.join(
            self.config["model_dir"],
            model_name,
            "metadata.json"
        )
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
            
    def get_model_metadata(self, model_name: str, version: Optional[str] = None) -> Dict[str, Any]:
        """
        Get metadata for a model.
        
        Args:
            model_name (str): Name of the model
            version (Optional[str]): Version of the model
            
        Returns:
            Dict[str, Any]: Model metadata
        """
        version = version or "latest"
        return self.model_metadata.get(f"{model_name}_{version}", {})
        
    def save_state(self, filepath: str) -> None:
        """
        Save manager state to file.
        
        Args:
            filepath (str): Path to save state
        """
        try:
            state = {
                "config": self.config,
                "model_versions": self.model_versions,
                "model_metadata": self.model_metadata
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
            self.model_versions = state["model_versions"]
            self.model_metadata = state["model_metadata"]
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}") 