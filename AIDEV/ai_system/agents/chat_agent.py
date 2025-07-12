from typing import Any, Dict, List, Optional
from openai import OpenAI
from .base_agent import BaseAgent
import json
import re
from datetime import datetime

class ChatAgent(BaseAgent):
    """
    Agent for handling chat interactions and conversations.
    Provides functionality for message processing, context management,
    and conversation history tracking.
    """
    
    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize the chat agent.
        
        Args:
            name (str): Name of the agent
            config (Dict[str, Any]): Configuration dictionary
        """
        super().__init__(name, config)
        self.client = OpenAI(api_key=config.get("openai_api_key"))
        self.model = config.get("model", "gpt-3.5-turbo")
        self.temperature = config.get("temperature", 0.7)
        self.max_tokens = config.get("max_tokens", 150)
        self.conversation_history = []
        self.context = {}
        self.max_history = config.get("max_history", 100)
        self.response_templates = config.get("response_templates", {})
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming chat message.
        
        Args:
            input_data (Dict[str, Any]): Input data containing message and context
            
        Returns:
            Dict[str, Any]: Response data
        """
        try:
            if not self._validate_input(input_data):
                return {"error": "Invalid input data"}
                
            message = input_data.get("message", "")
            context = input_data.get("context", {})
            
            # Update context
            self._update_context(context)
            
            # Process message
            response = await self._process_message(message)
            
            # Update conversation history
            self._update_history(message, response)
            
            return {
                "response": response,
                "context": self.context,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error processing message: {str(e)}")
            return {"error": str(e)}
            
    async def learn(self, data: Dict[str, Any]) -> None:
        """
        Learn from conversation data.
        
        Args:
            data (Dict[str, Any]): Learning data
        """
        try:
            # Extract patterns and responses
            patterns = data.get("patterns", [])
            responses = data.get("responses", [])
            
            # Update response templates
            for pattern, response in zip(patterns, responses):
                self.response_templates[pattern] = response
                
            # Save to memory
            self.memory["response_templates"] = self.response_templates
            
            self.logger.info(f"Learned {len(patterns)} new patterns")
            
        except Exception as e:
            self.logger.error(f"Error in learning: {str(e)}")
            
    def _process_message(self, message: str) -> str:
        """
        Process a single message and generate response.
        
        Args:
            message (str): Input message
            
        Returns:
            str: Generated response
        """
        # Check cache first
        cache_key = f"response_{hash(message)}"
        cached_response = self._get_cached_result(cache_key)
        if cached_response:
            return cached_response
            
        # Process message
        response = self._generate_response(message)
        
        # Cache response
        self._cache_result(cache_key, response)
        
        return response
        
    def _generate_response(self, message: str) -> str:
        """
        Generate response based on message and context.
        
        Args:
            message (str): Input message
            
        Returns:
            str: Generated response
        """
        # Check response templates
        for pattern, response in self.response_templates.items():
            if re.search(pattern, message, re.IGNORECASE):
                return response
                
        # Default response
        return "I'm not sure how to respond to that."
        
    def _update_context(self, new_context: Dict[str, Any]) -> None:
        """
        Update conversation context.
        
        Args:
            new_context (Dict[str, Any]): New context data
        """
        self.context.update(new_context)
        
    def _update_history(self, message: str, response: str) -> None:
        """
        Update conversation history.
        
        Args:
            message (str): User message
            response (str): Agent response
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "response": response,
            "context": self.context.copy()
        }
        
        self.conversation_history.append(entry)
        
        # Maintain history size limit
        if len(self.conversation_history) > self.max_history:
            self.conversation_history.pop(0)
            
    def get_conversation_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get conversation history.
        
        Args:
            limit (Optional[int]): Maximum number of entries to return
            
        Returns:
            List[Dict[str, Any]]: Conversation history
        """
        if limit is None:
            return self.conversation_history
        return self.conversation_history[-limit:]
        
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history = []
        self.logger.info("Conversation history cleared")
        
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
                "conversation_history": self.conversation_history,
                "context": self.context,
                "response_templates": self.response_templates
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
            self.conversation_history = state["conversation_history"]
            self.context = state["context"]
            self.response_templates = state["response_templates"]
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}") 