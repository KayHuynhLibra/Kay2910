from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent
import numpy as np
from datetime import datetime
import json

class LearningAgent(BaseAgent):
    """
    Agent for handling learning and model training.
    Provides functionality for data processing, model training,
    and performance evaluation.
    """
    
    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize the learning agent.
        
        Args:
            name (str): Name of the agent
            config (Dict[str, Any]): Configuration dictionary
        """
        super().__init__(name, config)
        self.models = {}
        self.training_history = []
        self.evaluation_metrics = {}
        self.max_training_history = config.get("max_training_history", 100)
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process learning request.
        
        Args:
            input_data (Dict[str, Any]): Input data containing learning parameters
            
        Returns:
            Dict[str, Any]: Learning results
        """
        try:
            if not self._validate_input(input_data):
                return {"error": "Invalid input data"}
                
            action = input_data.get("action")
            model_name = input_data.get("model_name")
            data = input_data.get("data", {})
            
            if action == "train":
                result = await self._train_model(model_name, data)
            elif action == "evaluate":
                result = await self._evaluate_model(model_name, data)
            elif action == "predict":
                result = await self._predict(model_name, data)
            else:
                return {"error": f"Unknown action: {action}"}
                
            return {
                "action": action,
                "model_name": model_name,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error processing learning request: {str(e)}")
            return {"error": str(e)}
            
    async def learn(self, data: Dict[str, Any]) -> None:
        """
        Learn from training data and update models.
        
        Args:
            data (Dict[str, Any]): Learning data
        """
        try:
            model_name = data.get("model_name")
            training_data = data.get("training_data")
            parameters = data.get("parameters", {})
            
            if not model_name or not training_data:
                raise ValueError("Missing model_name or training_data")
                
            # Update model
            await self._update_model(model_name, training_data, parameters)
            
            # Save to memory
            self.memory[f"model_{model_name}"] = {
                "parameters": parameters,
                "last_updated": datetime.now().isoformat()
            }
            
            self.logger.info(f"Model {model_name} updated successfully")
            
        except Exception as e:
            self.logger.error(f"Error in learning: {str(e)}")
            
    async def _train_model(self, model_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Train a model with given data.
        
        Args:
            model_name (str): Name of the model
            data (Dict[str, Any]): Training data
            
        Returns:
            Dict[str, Any]: Training results
        """
        try:
            # Prepare training data
            X = data.get("features")
            y = data.get("labels")
            parameters = data.get("parameters", {})
            
            # Train model
            model = self._get_or_create_model(model_name)
            model.fit(X, y, **parameters)
            
            # Update training history
            self._update_training_history(model_name, {
                "timestamp": datetime.now().isoformat(),
                "parameters": parameters,
                "metrics": model.get_metrics()
            })
            
            return {
                "status": "success",
                "metrics": model.get_metrics()
            }
            
        except Exception as e:
            self.logger.error(f"Error training model: {str(e)}")
            return {"error": str(e)}
            
    async def _evaluate_model(self, model_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate a model with given data.
        
        Args:
            model_name (str): Name of the model
            data (Dict[str, Any]): Evaluation data
            
        Returns:
            Dict[str, Any]: Evaluation results
        """
        try:
            # Prepare evaluation data
            X = data.get("features")
            y = data.get("labels")
            
            # Get model
            model = self._get_model(model_name)
            if not model:
                return {"error": f"Model {model_name} not found"}
                
            # Evaluate model
            metrics = model.evaluate(X, y)
            
            # Update evaluation metrics
            self.evaluation_metrics[model_name] = {
                "timestamp": datetime.now().isoformat(),
                "metrics": metrics
            }
            
            return {
                "status": "success",
                "metrics": metrics
            }
            
        except Exception as e:
            self.logger.error(f"Error evaluating model: {str(e)}")
            return {"error": str(e)}
            
    async def _predict(self, model_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make predictions using a model.
        
        Args:
            model_name (str): Name of the model
            data (Dict[str, Any]): Prediction data
            
        Returns:
            Dict[str, Any]: Prediction results
        """
        try:
            # Prepare prediction data
            X = data.get("features")
            
            # Get model
            model = self._get_model(model_name)
            if not model:
                return {"error": f"Model {model_name} not found"}
                
            # Make predictions
            predictions = model.predict(X)
            
            return {
                "status": "success",
                "predictions": predictions.tolist()
            }
            
        except Exception as e:
            self.logger.error(f"Error making predictions: {str(e)}")
            return {"error": str(e)}
            
    def _get_or_create_model(self, model_name: str) -> Any:
        """
        Get existing model or create new one.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            Any: Model instance
        """
        if model_name not in self.models:
            # Create new model based on configuration
            model_config = self.config.get("models", {}).get(model_name, {})
            model_type = model_config.get("type", "default")
            
            if model_type == "neural_network":
                from sklearn.neural_network import MLPClassifier
                self.models[model_name] = MLPClassifier(**model_config.get("parameters", {}))
            elif model_type == "random_forest":
                from sklearn.ensemble import RandomForestClassifier
                self.models[model_name] = RandomForestClassifier(**model_config.get("parameters", {}))
            else:
                from sklearn.linear_model import LogisticRegression
                self.models[model_name] = LogisticRegression(**model_config.get("parameters", {}))
                
        return self.models[model_name]
        
    def _get_model(self, model_name: str) -> Optional[Any]:
        """
        Get existing model.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            Optional[Any]: Model instance if exists, None otherwise
        """
        return self.models.get(model_name)
        
    def _update_training_history(self, model_name: str, entry: Dict[str, Any]) -> None:
        """
        Update training history.
        
        Args:
            model_name (str): Name of the model
            entry (Dict[str, Any]): Training history entry
        """
        if model_name not in self.training_history:
            self.training_history[model_name] = []
            
        self.training_history[model_name].append(entry)
        
        # Maintain history size limit
        if len(self.training_history[model_name]) > self.max_training_history:
            self.training_history[model_name].pop(0)
            
    def get_training_history(self, model_name: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get training history for a model.
        
        Args:
            model_name (str): Name of the model
            limit (Optional[int]): Maximum number of entries to return
            
        Returns:
            List[Dict[str, Any]]: Training history
        """
        history = self.training_history.get(model_name, [])
        if limit is None:
            return history
        return history[-limit:]
        
    def get_evaluation_metrics(self, model_name: str) -> Dict[str, Any]:
        """
        Get evaluation metrics for a model.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            Dict[str, Any]: Evaluation metrics
        """
        return self.evaluation_metrics.get(model_name, {})
        
    def save_state(self, filepath: str) -> None:
        """
        Save agent state to file.
        
        Args:
            filepath (str): Path to save state
        """
        try:
            state = {
                "name": self.name,
                "config": self.config,
                "memory": self.memory,
                "cache": self.cache,
                "training_history": self.training_history,
                "evaluation_metrics": self.evaluation_metrics
            }
            with open(filepath, 'w') as f:
                json.dump(state, f)
            self.logger.info(f"State saved to {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving state: {str(e)}")
            
    def load_state(self, filepath: str) -> None:
        """
        Load agent state from file.
        
        Args:
            filepath (str): Path to load state from
        """
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            self.name = state["name"]
            self.config = state["config"]
            self.memory = state["memory"]
            self.cache = state["cache"]
            self.training_history = state["training_history"]
            self.evaluation_metrics = state["evaluation_metrics"]
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}") 