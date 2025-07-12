from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy as np
from datetime import datetime

@dataclass
class Context:
    """Represents the context in which the AI system operates"""
    environment: Dict[str, Any]
    user_profile: Dict[str, Any]
    system_state: Dict[str, Any]
    timestamp: datetime = datetime.now()

class Model(ABC):
    """Abstract base class for AI models"""
    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        pass

    @abstractmethod
    def update(self, new_data: Any) -> None:
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        pass

class Behavior(ABC):
    """Abstract base class for system behaviors"""
    @abstractmethod
    def execute(self, context: Context, model_output: Any) -> Any:
        pass

    @abstractmethod
    def validate(self, context: Context) -> bool:
        pass

    @abstractmethod
    def get_constraints(self) -> Dict[str, Any]:
        pass

class MCBSystem:
    """Main MCB system implementation"""
    def __init__(self, model: Model, behavior: Behavior):
        self.model = model
        self.behavior = behavior
        self.context_history: List[Context] = []
        self.execution_history: List[Dict[str, Any]] = []

    def process(self, input_data: Any, context: Context) -> Dict[str, Any]:
        """
        Process input data with the given context
        
        Args:
            input_data: Input data for the model
            context: Current context of the system
            
        Returns:
            Dict containing the processing results
        """
        # Store context
        self.context_history.append(context)
        
        # Get model prediction
        model_output = self.model.predict(input_data)
        
        # Validate behavior
        if not self.behavior.validate(context):
            raise ValueError("Invalid context for current behavior")
        
        # Execute behavior
        result = self.behavior.execute(context, model_output)
        
        # Store execution history
        execution_record = {
            "timestamp": datetime.now(),
            "context": context,
            "model_output": model_output,
            "result": result,
            "model_metadata": self.model.get_metadata(),
            "behavior_constraints": self.behavior.get_constraints()
        }
        self.execution_history.append(execution_record)
        
        return result

    def get_system_state(self) -> Dict[str, Any]:
        """
        Get the current state of the MCB system
        
        Returns:
            Dict containing system state information
        """
        return {
            "context_history_size": len(self.context_history),
            "execution_history_size": len(self.execution_history),
            "model_metadata": self.model.get_metadata(),
            "behavior_constraints": self.behavior.get_constraints(),
            "last_context": self.context_history[-1] if self.context_history else None,
            "last_execution": self.execution_history[-1] if self.execution_history else None
        }

    def analyze_performance(self) -> Dict[str, Any]:
        """
        Analyze the performance of the MCB system
        
        Returns:
            Dict containing performance metrics
        """
        if not self.execution_history:
            return {"error": "No execution history available"}
            
        # Calculate basic metrics
        total_executions = len(self.execution_history)
        successful_executions = sum(1 for record in self.execution_history 
                                 if "error" not in record["result"])
        
        # Calculate average response time
        response_times = []
        for i in range(1, len(self.execution_history)):
            time_diff = (self.execution_history[i]["timestamp"] - 
                        self.execution_history[i-1]["timestamp"]).total_seconds()
            response_times.append(time_diff)
            
        avg_response_time = np.mean(response_times) if response_times else 0
        
        return {
            "total_executions": total_executions,
            "successful_executions": successful_executions,
            "success_rate": successful_executions / total_executions if total_executions > 0 else 0,
            "average_response_time": avg_response_time,
            "context_diversity": len(set(str(ctx) for ctx in self.context_history))
        } 