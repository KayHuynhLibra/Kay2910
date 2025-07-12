from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import logging
from datetime import datetime
import json

class BaseAgent(ABC):
    """
    Base class for all agents in the system.
    Provides common functionality for logging, error handling, and caching.
    """
    
    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize the base agent.
        
        Args:
            name (str): Name of the agent
            config (Dict[str, Any]): Configuration dictionary
        """
        self.name = name
        self.config = config
        self.memory = {}
        self.cache = {}
        self._setup_logging()
        self.status = "initialized"
        self.last_active = datetime.now()
        
    def _setup_logging(self) -> None:
        """Setup logging configuration for the agent."""
        self.logger = logging.getLogger(f"{self.name}_agent")
        self.logger.setLevel(logging.INFO)
        
        # Create handlers
        file_handler = logging.FileHandler(f"logs/{self.name}_agent.log")
        console_handler = logging.StreamHandler()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def _validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate input data.
        
        Args:
            input_data (Dict[str, Any]): Input data to validate
            
        Returns:
            bool: True if input is valid, False otherwise
        """
        try:
            required_fields = self.config.get("required_fields", [])
            for field in required_fields:
                if field not in input_data:
                    self.logger.error(f"Missing required field: {field}")
                    return False
            return True
        except Exception as e:
            self.logger.error(f"Error validating input: {str(e)}")
            return False
            
    def _cache_result(self, key: str, result: Any, ttl: int = 3600) -> None:
        """
        Cache a result with time-to-live.
        
        Args:
            key (str): Cache key
            result (Any): Result to cache
            ttl (int): Time to live in seconds
        """
        self.cache[key] = {
            "data": result,
            "timestamp": datetime.now().timestamp(),
            "ttl": ttl
        }
        
    def _get_cached_result(self, key: str) -> Optional[Any]:
        """
        Get a cached result if it exists and is not expired.
        
        Args:
            key (str): Cache key
            
        Returns:
            Optional[Any]: Cached result if valid, None otherwise
        """
        if key not in self.cache:
            return None
            
        cache_entry = self.cache[key]
        if datetime.now().timestamp() - cache_entry["timestamp"] > cache_entry["ttl"]:
            del self.cache[key]
            return None
            
        return cache_entry["data"]
        
    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process input data. Must be implemented by child classes.
        
        Args:
            input_data (Dict[str, Any]): Input data to process
            
        Returns:
            Dict[str, Any]: Processing result
        """
        pass
        
    @abstractmethod
    async def learn(self, data: Dict[str, Any]) -> None:
        """
        Learn from data. Must be implemented by child classes.
        
        Args:
            data (Dict[str, Any]): Data to learn from
        """
        pass
        
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
                "cache": self.cache
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
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}")
            
    def clear_cache(self) -> None:
        """Clear the agent's cache."""
        self.cache = {}
        self.logger.info("Cache cleared")
        
    def clear_memory(self) -> None:
        """Clear the agent's memory."""
        self.memory = {}
        self.logger.info("Memory cleared")
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "name": self.name,
            "status": self.status,
            "last_active": self.last_active.isoformat(),
            "memory_size": len(self.memory)
        }
    
    def add_to_memory(self, item: Any) -> None:
        """Add item to agent's memory"""
        self.memory.append({
            "timestamp": datetime.now().isoformat(),
            "data": item
        })
        # Keep memory size limited
        if len(self.memory) > self.config.get("max_memory_size", 1000):
            self.memory.pop(0)
    
    def get_memory(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get agent's memory with optional limit"""
        if limit is None:
            return self.memory
        return self.memory[-limit:]
    
    async def start(self) -> None:
        """Start the agent"""
        self.status = "running"
        self.logger.info(f"Agent {self.name} started")
    
    async def stop(self) -> None:
        """Stop the agent"""
        self.status = "stopped"
        self.logger.info(f"Agent {self.name} stopped")
    
    def update_status(self, new_status: str) -> None:
        """Update agent status"""
        self.status = new_status
        self.last_active = datetime.now()
        self.logger.info(f"Agent {self.name} status updated to {new_status}") 