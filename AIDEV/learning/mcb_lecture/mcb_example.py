from typing import Dict, Any, List
import numpy as np
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Context:
    """Represents the context in which the AI system operates"""
    environment: Dict[str, Any]
    user_profile: Dict[str, Any]
    system_state: Dict[str, Any]

class Model(ABC):
    """Abstract base class for AI models"""
    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        pass

    @abstractmethod
    def update(self, new_data: Any) -> None:
        pass

class Behavior(ABC):
    """Abstract base class for system behaviors"""
    @abstractmethod
    def execute(self, context: Context, model_output: Any) -> Any:
        pass

    @abstractmethod
    def validate(self, context: Context) -> bool:
        pass

class SimpleModel(Model):
    """A simple implementation of the Model class"""
    def __init__(self):
        self.weights = np.random.randn(10)
    
    def predict(self, input_data: np.ndarray) -> float:
        return np.dot(input_data, self.weights)
    
    def update(self, new_data: np.ndarray) -> None:
        # Simple update rule for demonstration
        self.weights += 0.01 * new_data

class SimpleBehavior(Behavior):
    """A simple implementation of the Behavior class"""
    def execute(self, context: Context, model_output: float) -> Dict[str, Any]:
        # Example behavior execution
        return {
            "action": "recommend" if model_output > 0.5 else "reject",
            "confidence": abs(model_output),
            "context_used": context.environment
        }
    
    def validate(self, context: Context) -> bool:
        # Example validation
        return all(key in context.environment for key in ["temperature", "humidity"])

class MCBSystem:
    """Main MCB system implementation"""
    def __init__(self, model: Model, behavior: Behavior):
        self.model = model
        self.behavior = behavior
        self.context_history: List[Context] = []

    def process(self, input_data: np.ndarray, context: Context) -> Dict[str, Any]:
        # Store context
        self.context_history.append(context)
        
        # Get model prediction
        model_output = self.model.predict(input_data)
        
        # Validate behavior
        if not self.behavior.validate(context):
            raise ValueError("Invalid context for current behavior")
        
        # Execute behavior
        result = self.behavior.execute(context, model_output)
        
        # Update model if needed
        if result["confidence"] < 0.7:
            self.model.update(input_data)
        
        return result

def main():
    # Create instances
    model = SimpleModel()
    behavior = SimpleBehavior()
    system = MCBSystem(model, behavior)
    
    # Example usage
    input_data = np.random.randn(10)
    context = Context(
        environment={"temperature": 25, "humidity": 60},
        user_profile={"age": 30, "preferences": ["tech", "sports"]},
        system_state={"mode": "normal", "load": 0.5}
    )
    
    try:
        result = system.process(input_data, context)
        print("System output:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main() 