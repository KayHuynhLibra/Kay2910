#!/usr/bin/env python3
"""
Advanced AI 2025 - Các công nghệ AI tiên tiến
Bao gồm: AI Agents, Multimodal AI, Edge AI, và các xu hướng mới nhất
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import json
import logging
import asyncio
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import cv2
import speech_recognition as sr
from PIL import Image
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time
import random

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaskType(Enum):
    """Các loại task mà AI Agent có thể thực hiện"""
    TEXT_GENERATION = "text_generation"
    IMAGE_ANALYSIS = "image_analysis"
    SPEECH_RECOGNITION = "speech_recognition"
    CODE_GENERATION = "code_generation"
    DATA_ANALYSIS = "data_analysis"
    WEB_SEARCH = "web_search"
    FILE_OPERATION = "file_operation"

@dataclass
class AgentMemory:
    """Bộ nhớ của AI Agent"""
    short_term: List[Dict] = field(default_factory=list)
    long_term: Dict[str, Any] = field(default_factory=dict)
    context_window: int = 1000
    
    def add_memory(self, memory: Dict):
        """Thêm memory mới"""
        self.short_term.append(memory)
        if len(self.short_term) > self.context_window:
            self.short_term.pop(0)
    
    def get_relevant_memories(self, query: str, limit: int = 5) -> List[Dict]:
        """Lấy memories liên quan đến query"""
        # Mô phỏng semantic search
        relevant = []
        for memory in self.short_term[-limit:]:
            if query.lower() in str(memory).lower():
                relevant.append(memory)
        return relevant

@dataclass
class Tool:
    """Công cụ mà AI Agent có thể sử dụng"""
    name: str
    description: str
    task_type: TaskType
    function: callable
    parameters: Dict[str, Any] = field(default_factory=dict)

class AIAgent:
    """AI Agent tiên tiến với khả năng đa nhiệm"""
    
    def __init__(self, name: str = "AI_Agent_2025"):
        self.name = name
        self.memory = AgentMemory()
        self.tools = {}
        self.planner = None
        self.executor = None
        self._setup_agent()
    
    def _setup_agent(self):
        """Thiết lập các thành phần của agent"""
        # Setup tools
        self._setup_tools()
        
        # Setup planner
        self.planner = TaskPlanner()
        
        # Setup executor
        self.executor = TaskExecutor(self.tools)
    
    def _setup_tools(self):
        """Thiết lập các công cụ"""
        # Text generation tool
        self.tools['text_generator'] = Tool(
            name="text_generator",
            description="Generate human-like text",
            task_type=TaskType.TEXT_GENERATION,
            function=self._generate_text
        )
        
        # Image analysis tool
        self.tools['image_analyzer'] = Tool(
            name="image_analyzer",
            description="Analyze images and extract information",
            task_type=TaskType.IMAGE_ANALYSIS,
            function=self._analyze_image
        )
        
        # Speech recognition tool
        self.tools['speech_recognizer'] = Tool(
            name="speech_recognizer",
            description="Convert speech to text",
            task_type=TaskType.SPEECH_RECOGNITION,
            function=self._recognize_speech
        )
        
        # Code generation tool
        self.tools['code_generator'] = Tool(
            name="code_generator",
            description="Generate code based on requirements",
            task_type=TaskType.CODE_GENERATION,
            function=self._generate_code
        )
        
        # Data analysis tool
        self.tools['data_analyzer'] = Tool(
            name="data_analyzer",
            description="Analyze and visualize data",
            task_type=TaskType.DATA_ANALYSIS,
            function=self._analyze_data
        )
    
    async def process_request(self, request: str) -> Dict[str, Any]:
        """Xử lý yêu cầu từ người dùng"""
        logger.info(f"Agent {self.name} processing request: {request}")
        
        # 1. Add to memory
        self.memory.add_memory({
            'type': 'user_request',
            'content': request,
            'timestamp': time.time()
        })
        
        # 2. Plan execution
        plan = self.planner.create_plan(request, self.tools)
        
        # 3. Execute plan
        results = await self.executor.execute_plan(plan)
        
        # 4. Update memory with results
        self.memory.add_memory({
            'type': 'execution_result',
            'content': results,
            'timestamp': time.time()
        })
        
        return {
            'request': request,
            'plan': plan,
            'results': results,
            'agent_name': self.name
        }
    
    def _generate_text(self, prompt: str, max_length: int = 100) -> str:
        """Generate text"""
        # Mô phỏng text generation
        responses = [
            f"Based on your request '{prompt}', here is a comprehensive response...",
            f"I understand you're asking about '{prompt}'. Let me provide detailed information...",
            f"Regarding '{prompt}', I can help you with the following insights...",
            f"For your question about '{prompt}', here's what I found..."
        ]
        return np.random.choice(responses)
    
    def _analyze_image(self, image_path: str) -> Dict[str, Any]:
        """Analyze image"""
        # Mô phỏng image analysis
        analysis = {
            'objects_detected': ['person', 'car', 'building'],
            'scene_description': 'Urban street scene with people and vehicles',
            'colors': ['blue', 'gray', 'white'],
            'confidence': 0.85
        }
        return analysis
    
    def _recognize_speech(self, audio_path: str) -> str:
        """Recognize speech"""
        # Mô phỏng speech recognition
        transcriptions = [
            "Hello, how can I help you today?",
            "I need assistance with my project",
            "What is the weather like?",
            "Can you explain this concept?"
        ]
        return np.random.choice(transcriptions)
    
    def _generate_code(self, requirements: str, language: str = "python") -> str:
        """Generate code"""
        # Mô phỏng code generation
        code_templates = {
            "python": f"""
# Generated code for: {requirements}
def main():
    print("Hello, World!")
    # Implementation for {requirements}
    
if __name__ == "__main__":
    main()
""",
            "javascript": f"""
// Generated code for: {requirements}
function main() {{
    console.log("Hello, World!");
    // Implementation for {requirements}
}}

main();
"""
        }
        return code_templates.get(language, code_templates["python"])
    
    def _analyze_data(self, data: List[float]) -> Dict[str, Any]:
        """Analyze data"""
        # Mô phỏng data analysis
        analysis = {
            'mean': np.mean(data),
            'std': np.std(data),
            'min': np.min(data),
            'max': np.max(data),
            'trend': 'increasing' if len(data) > 1 and data[-1] > data[0] else 'decreasing'
        }
        return analysis

class TaskPlanner:
    """Planner để tạo kế hoạch thực hiện task"""
    
    def create_plan(self, request: str, tools: Dict[str, Tool]) -> List[Dict]:
        """Tạo kế hoạch thực hiện"""
        plan = []
        
        # Simple rule-based planning
        if "text" in request.lower() or "write" in request.lower():
            plan.append({
                'tool': 'text_generator',
                'parameters': {'prompt': request, 'max_length': 200},
                'description': 'Generate text response'
            })
        
        if "image" in request.lower() or "picture" in request.lower():
            plan.append({
                'tool': 'image_analyzer',
                'parameters': {'image_path': 'sample_image.jpg'},
                'description': 'Analyze image content'
            })
        
        if "speech" in request.lower() or "audio" in request.lower():
            plan.append({
                'tool': 'speech_recognizer',
                'parameters': {'audio_path': 'sample_audio.wav'},
                'description': 'Convert speech to text'
            })
        
        if "code" in request.lower() or "program" in request.lower():
            plan.append({
                'tool': 'code_generator',
                'parameters': {'requirements': request, 'language': 'python'},
                'description': 'Generate code'
            })
        
        if "data" in request.lower() or "analyze" in request.lower():
            plan.append({
                'tool': 'data_analyzer',
                'parameters': {'data': [1, 2, 3, 4, 5]},
                'description': 'Analyze data'
            })
        
        # Default to text generation if no specific tool identified
        if not plan:
            plan.append({
                'tool': 'text_generator',
                'parameters': {'prompt': request, 'max_length': 150},
                'description': 'Generate general response'
            })
        
        return plan

class TaskExecutor:
    """Executor để thực hiện các task"""
    
    def __init__(self, tools: Dict[str, Tool]):
        self.tools = tools
    
    async def execute_plan(self, plan: List[Dict]) -> List[Dict]:
        """Thực hiện kế hoạch"""
        results = []
        
        for step in plan:
            tool_name = step['tool']
            parameters = step['parameters']
            
            if tool_name in self.tools:
                tool = self.tools[tool_name]
                try:
                    result = tool.function(**parameters)
                    results.append({
                        'step': step['description'],
                        'tool': tool_name,
                        'result': result,
                        'status': 'success'
                    })
                except Exception as e:
                    results.append({
                        'step': step['description'],
                        'tool': tool_name,
                        'error': str(e),
                        'status': 'failed'
                    })
            else:
                results.append({
                    'step': step['description'],
                    'tool': tool_name,
                    'error': 'Tool not found',
                    'status': 'failed'
                })
        
        return results

class MultimodalAI:
    """Multimodal AI system"""
    
    def __init__(self):
        self.text_processor = None
        self.image_processor = None
        self.audio_processor = None
        self.fusion_model = None
        self._setup_processors()
    
    def _setup_processors(self):
        """Thiết lập các processor"""
        # Text processor
        self.text_processor = self._create_text_processor()
        
        # Image processor (mô phỏng)
        self.image_processor = self._create_image_processor()
        
        # Audio processor (mô phỏng)
        self.audio_processor = self._create_audio_processor()
        
        # Fusion model
        self.fusion_model = self._create_fusion_model()
    
    def _create_text_processor(self):
        """Tạo text processor"""
        class TextProcessor:
            def process(self, text):
                return {
                    'features': np.random.randn(100),
                    'sentiment': 'neutral'
                }
        return TextProcessor()
    
    def _create_image_processor(self):
        """Tạo image processor"""
        class ImageProcessor:
            def process(self, image):
                return {
                    'features': np.random.randn(512),
                    'objects': ['person', 'car', 'building'],
                    'scene': 'urban'
                }
        return ImageProcessor()
    
    def _create_audio_processor(self):
        """Tạo audio processor"""
        class AudioProcessor:
            def process(self, audio):
                return {
                    'features': np.random.randn(256),
                    'transcript': 'Sample audio transcript',
                    'emotion': 'neutral'
                }
        return AudioProcessor()
    
    def _create_fusion_model(self):
        """Tạo fusion model"""
        class FusionModel:
            def fuse(self, text_features, image_features, audio_features):
                # Mô phỏng fusion
                combined = np.concatenate([text_features, image_features, audio_features])
                return {
                    'fused_features': combined,
                    'confidence': 0.9,
                    'interpretation': 'Multimodal understanding completed'
                }
        return FusionModel()
    
    def process_multimodal(self, text: str = None, image: str = None, audio: str = None) -> Dict:
        """Xử lý dữ liệu đa phương tiện"""
        results = {}
        
        if text:
            text_result = self.text_processor.process(text)
            results['text'] = text_result
        
        if image:
            image_result = self.image_processor.process(image)
            results['image'] = image_result
        
        if audio:
            audio_result = self.audio_processor.process(audio)
            results['audio'] = audio_result
        
        # Fusion if multiple modalities
        if len(results) > 1:
            fusion_result = self.fusion_model.fuse(
                results.get('text', np.zeros(100)),
                results.get('image', {}).get('features', np.zeros(512)),
                results.get('audio', {}).get('features', np.zeros(256))
            )
            results['fusion'] = fusion_result
        
        return results

class EdgeAI:
    """Edge AI system cho thiết bị edge"""
    
    def __init__(self, device_type: str = "mobile"):
        self.device_type = device_type
        self.model = None
        self.optimizer = None
        self._setup_edge_model()
    
    def _setup_edge_model(self):
        """Thiết lập model cho edge device"""
        # Lightweight model cho edge
        class EdgeModel(nn.Module):
            def __init__(self, input_size=100, hidden_size=50, output_size=10):
                super().__init__()
                self.fc1 = nn.Linear(input_size, hidden_size)
                self.fc2 = nn.Linear(hidden_size, output_size)
                self.relu = nn.ReLU()
                self.dropout = nn.Dropout(0.1)
            
            def forward(self, x):
                x = self.relu(self.fc1(x))
                x = self.dropout(x)
                return self.fc2(x)
        
        self.model = EdgeModel()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
    
    def train_on_device(self, data: torch.Tensor, labels: torch.Tensor):
        """Train model trên thiết bị"""
        self.model.train()
        self.optimizer.zero_grad()
        
        outputs = self.model(data)
        loss = nn.CrossEntropyLoss()(outputs, labels)
        loss.backward()
        self.optimizer.step()
        
        return loss.item()
    
    def inference(self, data: torch.Tensor) -> torch.Tensor:
        """Inference trên thiết bị"""
        self.model.eval()
        with torch.no_grad():
            return self.model(data)
    
    def get_model_size(self) -> int:
        """Lấy kích thước model"""
        param_size = 0
        for param in self.model.parameters():
            param_size += param.nelement() * param.element_size()
        buffer_size = 0
        for buffer in self.model.buffers():
            buffer_size += buffer.nelement() * buffer.element_size()
        return param_size + buffer_size

async def demo_advanced_ai():
    """Demo các công nghệ AI tiên tiến"""
    print("🚀 Advanced AI 2025 Demo")
    print("=" * 50)
    
    # 1. AI Agent Demo
    print("\n🤖 1. AI Agent với Planning và Execution:")
    agent = AIAgent("SmartAgent_2025")
    
    requests = [
        "Generate a text about artificial intelligence",
        "Analyze this image for me",
        "Write Python code for a simple calculator",
        "Analyze this dataset: [1, 2, 3, 4, 5]"
    ]
    
    for request in requests:
        result = await agent.process_request(request)
        print(f"  Request: {request}")
        print(f"  Plan: {len(result['plan'])} steps")
        print(f"  Results: {len(result['results'])} completed")
        print()
    
    # 2. Multimodal AI Demo
    print("\n🎨 2. Multimodal AI Processing:")
    multimodal_ai = MultimodalAI()
    
    multimodal_result = multimodal_ai.process_multimodal(
        text="A cat sitting on a chair",
        image="sample_image.jpg",
        audio="sample_audio.wav"
    )
    
    print(f"  Text processing: {'text' in multimodal_result}")
    print(f"  Image processing: {'image' in multimodal_result}")
    print(f"  Audio processing: {'audio' in multimodal_result}")
    print(f"  Fusion completed: {'fusion' in multimodal_result}")
    
    # 3. Edge AI Demo
    print("\n📱 3. Edge AI trên thiết bị di động:")
    edge_ai = EdgeAI("mobile")
    
    # Simulate training data
    data = torch.randn(10, 100)
    labels = torch.randint(0, 10, (10,))
    
    # Train on device
    loss = edge_ai.train_on_device(data, labels)
    print(f"  Training loss: {loss:.4f}")
    
    # Inference
    test_data = torch.randn(1, 100)
    prediction = edge_ai.inference(test_data)
    print(f"  Prediction shape: {prediction.shape}")
    
    # Model size
    model_size = edge_ai.get_model_size()
    print(f"  Model size: {model_size / 1024:.2f} KB")
    
    print("\n🎉 Demo hoàn thành!")
    print("\n💡 Các công nghệ này đại diện cho xu hướng AI 2025:")
    print("  - AI Agents: Autonomous systems với planning")
    print("  - Multimodal AI: Xử lý đa phương tiện")
    print("  - Edge AI: AI trên thiết bị edge")
    print("  - Federated Learning: Bảo vệ privacy")

if __name__ == "__main__":
    asyncio.run(demo_advanced_ai()) 