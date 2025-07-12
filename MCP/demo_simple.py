#!/usr/bin/env python3
"""
Demo đơn giản - AI 2025 với MCP
Thử nghiệm các tính năng cơ bản
"""

import torch
import numpy as np
import json
from datetime import datetime

def test_basic_ai():
    """Test các tính năng AI cơ bản"""
    print("=" * 50)
    print("AI 2025 với MCP - Demo đơn giản")
    print("=" * 50)
    
    # 1. Test PyTorch
    print("\n1. PyTorch Test:")
    x = torch.randn(3, 3)
    y = torch.randn(3, 3)
    z = torch.mm(x, y)
    print(f"   Matrix multiplication: {z.shape}")
    print(f"   PyTorch version: {torch.__version__}")
    
    # 2. Test NumPy
    print("\n2. NumPy Test:")
    arr = np.random.randn(5, 5)
    print(f"   Random array shape: {arr.shape}")
    print(f"   Mean: {arr.mean():.4f}")
    print(f"   Std: {arr.std():.4f}")
    
    # 3. Test JSON
    print("\n3. JSON Test:")
    data = {
        "project": "AI 2025 với MCP",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "features": ["MCP", "AI Training", "Multimodal", "Edge AI"]
    }
    print(f"   Data: {json.dumps(data, indent=2, ensure_ascii=False)}")
    
    # 4. Test MCP Simulation
    print("\n4. MCP Simulation:")
    
    class SimpleMCPServer:
        def __init__(self):
            self.resources = {
                "database": {"type": "sqlite", "tables": ["users", "products"]},
                "filesystem": {"type": "local", "root": "./data"},
                "api": {"type": "rest", "endpoints": ["/users", "/products"]}
            }
            self.tools = {
                "analyze_data": "Data analysis tool",
                "process_file": "File processing tool"
            }
        
        def list_resources(self):
            return list(self.resources.keys())
        
        def list_tools(self):
            return list(self.tools.keys())
        
        def call_tool(self, tool_name, params):
            if tool_name == "analyze_data":
                return f"Analyzed data with params: {params}"
            elif tool_name == "process_file":
                return f"Processed file with params: {params}"
            else:
                return f"Unknown tool: {tool_name}"
    
    # Tạo MCP server mô phỏng
    mcp_server = SimpleMCPServer()
    
    print(f"   Resources: {mcp_server.list_resources()}")
    print(f"   Tools: {mcp_server.list_tools()}")
    
    # Test tool calls
    result1 = mcp_server.call_tool("analyze_data", {"dataset": "sales", "operation": "summary"})
    result2 = mcp_server.call_tool("process_file", {"file": "data.json", "operation": "read"})
    
    print(f"   Tool result 1: {result1}")
    print(f"   Tool result 2: {result2}")
    
    # 5. Test AI Training Simulation
    print("\n5. AI Training Simulation:")
    
    # Mô phỏng training loop
    epochs = 3
    for epoch in range(epochs):
        # Mô phỏng loss
        loss = 1.0 / (epoch + 1) + np.random.normal(0, 0.1)
        accuracy = 0.8 + epoch * 0.05 + np.random.normal(0, 0.02)
        
        print(f"   Epoch {epoch + 1}/{epochs}: Loss={loss:.4f}, Accuracy={accuracy:.4f}")
    
    print("\n" + "=" * 50)
    print("Demo hoàn thành thành công!")
    print("=" * 50)

def test_multimodal_simulation():
    """Test multimodal AI simulation"""
    print("\n" + "=" * 50)
    print("Multimodal AI Simulation")
    print("=" * 50)
    
    # Mô phỏng text processing
    print("\n1. Text Processing:")
    text = "AI 2025 với MCP là tương lai của AI"
    print(f"   Input text: {text}")
    print(f"   Text length: {len(text)} characters")
    print(f"   Word count: {len(text.split())} words")
    
    # Mô phỏng image processing
    print("\n2. Image Processing:")
    image_size = (224, 224, 3)
    print(f"   Image size: {image_size}")
    print(f"   Total pixels: {image_size[0] * image_size[1]}")
    print(f"   Channels: {image_size[2]}")
    
    # Mô phỏng audio processing
    print("\n3. Audio Processing:")
    audio_duration = 10.5  # seconds
    sample_rate = 16000
    print(f"   Audio duration: {audio_duration} seconds")
    print(f"   Sample rate: {sample_rate} Hz")
    print(f"   Total samples: {int(audio_duration * sample_rate)}")
    
    # Mô phỏng fusion
    print("\n4. Multimodal Fusion:")
    text_features = np.random.randn(512)
    image_features = np.random.randn(512)
    audio_features = np.random.randn(256)
    
    # Fusion
    fused_features = np.concatenate([text_features, image_features, audio_features])
    print(f"   Text features: {text_features.shape}")
    print(f"   Image features: {image_features.shape}")
    print(f"   Audio features: {audio_features.shape}")
    print(f"   Fused features: {fused_features.shape}")
    
    print("\n" + "=" * 50)
    print("Multimodal simulation hoàn thành!")
    print("=" * 50)

def test_edge_ai_simulation():
    """Test Edge AI simulation"""
    print("\n" + "=" * 50)
    print("Edge AI Simulation")
    print("=" * 50)
    
    # Mô phỏng lightweight model
    print("\n1. Lightweight Model:")
    input_size = 100
    hidden_size = 50
    output_size = 10
    
    # Tính toán model size
    total_params = input_size * hidden_size + hidden_size * output_size + hidden_size + output_size
    model_size_mb = total_params * 4 / (1024 * 1024)  # 4 bytes per parameter
    
    print(f"   Input size: {input_size}")
    print(f"   Hidden size: {hidden_size}")
    print(f"   Output size: {output_size}")
    print(f"   Total parameters: {total_params:,}")
    print(f"   Model size: {model_size_mb:.2f} MB")
    
    # Mô phỏng inference time
    print("\n2. Inference Performance:")
    batch_sizes = [1, 4, 8, 16]
    
    for batch_size in batch_sizes:
        # Mô phỏng inference time (milliseconds)
        inference_time = 5 + batch_size * 2 + np.random.normal(0, 1)
        throughput = batch_size / (inference_time / 1000)  # samples per second
        
        print(f"   Batch size {batch_size}: {inference_time:.1f}ms, {throughput:.1f} samples/sec")
    
    # Mô phỏng power consumption
    print("\n3. Power Consumption:")
    power_consumption = 0.5  # Watts
    print(f"   Power consumption: {power_consumption}W")
    print(f"   Energy efficient: {'Yes' if power_consumption < 1.0 else 'No'}")
    
    print("\n" + "=" * 50)
    print("Edge AI simulation hoàn thành!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        # Chạy các test
        test_basic_ai()
        test_multimodal_simulation()
        test_edge_ai_simulation()
        
        print("\n🎉 Tất cả tests đã hoàn thành thành công!")
        print("🚀 Bạn đã sẵn sàng cho hành trình AI 2025!")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        print("💡 Hãy kiểm tra lại cài đặt dependencies") 