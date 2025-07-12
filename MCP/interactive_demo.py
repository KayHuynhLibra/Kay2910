#!/usr/bin/env python3
"""
Interactive Demo - AI 2025 với MCP
Demo tương tác để thử nghiệm các tính năng
"""

import json
import numpy as np
import torch
from datetime import datetime

class InteractiveMCPServer:
    """MCP Server tương tác"""
    
    def __init__(self):
        self.resources = {
            "database": {
                "type": "sqlite",
                "tables": ["users", "products", "orders"],
                "data": self._load_sample_data()
            },
            "filesystem": {
                "type": "local",
                "root": "./data",
                "files": ["sample_data.json", "config.json"]
            },
            "api": {
                "type": "rest",
                "endpoints": ["/users", "/products", "/analytics"],
                "status": "online"
            }
        }
        
        self.tools = {
            "analyze_data": {
                "description": "Phân tích dữ liệu",
                "parameters": ["dataset", "operation"]
            },
            "process_file": {
                "description": "Xử lý file",
                "parameters": ["file_path", "operation"]
            },
            "generate_text": {
                "description": "Tạo văn bản",
                "parameters": ["prompt", "max_length"]
            },
            "train_model": {
                "description": "Huấn luyện model",
                "parameters": ["model_type", "epochs"]
            }
        }
        
        self.memory = []
    
    def _load_sample_data(self):
        """Load dữ liệu mẫu"""
        try:
            with open("data/sample_data.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"error": "Không thể load dữ liệu"}
    
    def list_resources(self):
        """Liệt kê tài nguyên"""
        return list(self.resources.keys())
    
    def read_resource(self, resource_name):
        """Đọc tài nguyên"""
        if resource_name in self.resources:
            return self.resources[resource_name]
        return {"error": f"Tài nguyên {resource_name} không tồn tại"}
    
    def list_tools(self):
        """Liệt kê công cụ"""
        return list(self.tools.keys())
    
    def call_tool(self, tool_name, parameters):
        """Gọi công cụ"""
        if tool_name not in self.tools:
            return {"error": f"Công cụ {tool_name} không tồn tại"}
        
        # Log tool call
        self.memory.append({
            "timestamp": datetime.now().isoformat(),
            "tool": tool_name,
            "parameters": parameters
        })
        
        # Execute tool
        if tool_name == "analyze_data":
            return self._analyze_data(parameters)
        elif tool_name == "process_file":
            return self._process_file(parameters)
        elif tool_name == "generate_text":
            return self._generate_text(parameters)
        elif tool_name == "train_model":
            return self._train_model(parameters)
    
    def _analyze_data(self, params):
        """Phân tích dữ liệu"""
        dataset = params.get("dataset", "users")
        operation = params.get("operation", "summary")
        
        if dataset in self.resources["database"]["data"]:
            data = self.resources["database"]["data"][dataset]
            
            if operation == "summary":
                return {
                    "dataset": dataset,
                    "count": len(data),
                    "operation": operation,
                    "summary": f"Dataset {dataset} có {len(data)} records"
                }
            elif operation == "statistics":
                if dataset == "products":
                    prices = [item["price"] for item in data]
                    return {
                        "dataset": dataset,
                        "count": len(data),
                        "avg_price": np.mean(prices),
                        "min_price": np.min(prices),
                        "max_price": np.max(prices)
                    }
        
        return {"error": f"Không thể phân tích dataset {dataset}"}
    
    def _process_file(self, params):
        """Xử lý file"""
        file_path = params.get("file_path", "")
        operation = params.get("operation", "read")
        
        if operation == "read":
            if file_path == "sample_data.json":
                return {
                    "file": file_path,
                    "operation": operation,
                    "content": "Dữ liệu mẫu đã được đọc thành công"
                }
        
        return {
            "file": file_path,
            "operation": operation,
            "status": "completed"
        }
    
    def _generate_text(self, params):
        """Tạo văn bản"""
        prompt = params.get("prompt", "")
        max_length = params.get("max_length", 100)
        
        # Mô phỏng text generation
        responses = [
            f"Dựa trên prompt '{prompt}', đây là một phản hồi mẫu về AI 2025.",
            f"AI 2025 với MCP sẽ cách mạng hóa cách chúng ta tương tác với máy tính.",
            f"Model Context Protocol (MCP) là tương lai của AI integration.",
            f"Multimodal AI sẽ cho phép xử lý text, image, audio và video cùng lúc."
        ]
        
        import random
        response = random.choice(responses)
        
        return {
            "prompt": prompt,
            "response": response[:max_length],
            "length": len(response[:max_length])
        }
    
    def _train_model(self, params):
        """Huấn luyện model"""
        model_type = params.get("model_type", "transformer")
        epochs = params.get("epochs", 3)
        
        # Mô phỏng training
        training_log = []
        for epoch in range(epochs):
            loss = 1.0 / (epoch + 1) + np.random.normal(0, 0.1)
            accuracy = 0.8 + epoch * 0.05 + np.random.normal(0, 0.02)
            
            training_log.append({
                "epoch": epoch + 1,
                "loss": round(loss, 4),
                "accuracy": round(accuracy, 4)
            })
        
        return {
            "model_type": model_type,
            "epochs": epochs,
            "training_log": training_log,
            "final_accuracy": training_log[-1]["accuracy"]
        }
    
    def get_memory(self):
        """Lấy lịch sử hoạt động"""
        return self.memory

def print_menu():
    """In menu chính"""
    print("\n" + "="*60)
    print("🚀 AI 2025 với MCP - Interactive Demo")
    print("="*60)
    print("1. Liệt kê tài nguyên")
    print("2. Đọc tài nguyên")
    print("3. Liệt kê công cụ")
    print("4. Phân tích dữ liệu")
    print("5. Xử lý file")
    print("6. Tạo văn bản")
    print("7. Huấn luyện model")
    print("8. Xem lịch sử")
    print("9. Thoát")
    print("="*60)

def main():
    """Hàm chính"""
    print("🎉 Chào mừng đến với AI 2025 với MCP!")
    print("💡 Đây là demo tương tác để thử nghiệm các tính năng")
    
    # Khởi tạo MCP server
    mcp_server = InteractiveMCPServer()
    
    while True:
        print_menu()
        
        try:
            choice = input("Chọn tùy chọn (1-9): ").strip()
            
            if choice == "1":
                # Liệt kê tài nguyên
                resources = mcp_server.list_resources()
                print(f"\n📋 Tài nguyên có sẵn: {resources}")
                
            elif choice == "2":
                # Đọc tài nguyên
                resource_name = input("Nhập tên tài nguyên (database/filesystem/api): ").strip()
                result = mcp_server.read_resource(resource_name)
                print(f"\n📖 Kết quả: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
            elif choice == "3":
                # Liệt kê công cụ
                tools = mcp_server.list_tools()
                print(f"\n🛠️ Công cụ có sẵn:")
                for tool in tools:
                    print(f"   - {tool}: {mcp_server.tools[tool]['description']}")
                
            elif choice == "4":
                # Phân tích dữ liệu
                dataset = input("Nhập dataset (users/products/orders): ").strip()
                operation = input("Nhập operation (summary/statistics): ").strip()
                
                result = mcp_server.call_tool("analyze_data", {
                    "dataset": dataset,
                    "operation": operation
                })
                print(f"\n📊 Kết quả phân tích: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
            elif choice == "5":
                # Xử lý file
                file_path = input("Nhập đường dẫn file: ").strip()
                operation = input("Nhập operation (read/write): ").strip()
                
                result = mcp_server.call_tool("process_file", {
                    "file_path": file_path,
                    "operation": operation
                })
                print(f"\n📁 Kết quả xử lý file: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
            elif choice == "6":
                # Tạo văn bản
                prompt = input("Nhập prompt: ").strip()
                max_length = int(input("Nhập độ dài tối đa (số): ").strip())
                
                result = mcp_server.call_tool("generate_text", {
                    "prompt": prompt,
                    "max_length": max_length
                })
                print(f"\n📝 Kết quả tạo văn bản: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
            elif choice == "7":
                # Huấn luyện model
                model_type = input("Nhập loại model (transformer/cnn/rnn): ").strip()
                epochs = int(input("Nhập số epochs (số): ").strip())
                
                result = mcp_server.call_tool("train_model", {
                    "model_type": model_type,
                    "epochs": epochs
                })
                print(f"\n🧠 Kết quả huấn luyện: {json.dumps(result, indent=2, ensure_ascii=False)}")
                
            elif choice == "8":
                # Xem lịch sử
                memory = mcp_server.get_memory()
                print(f"\n📚 Lịch sử hoạt động:")
                for i, record in enumerate(memory[-5:], 1):  # Hiển thị 5 record gần nhất
                    print(f"   {i}. {record['timestamp']} - {record['tool']}: {record['parameters']}")
                
            elif choice == "9":
                # Thoát
                print("\n👋 Cảm ơn bạn đã thử nghiệm AI 2025 với MCP!")
                print("🚀 Hẹn gặp lại trong hành trình AI!")
                break
                
            else:
                print("❌ Lựa chọn không hợp lệ. Vui lòng chọn từ 1-9.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Tạm biệt!")
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            print("💡 Vui lòng thử lại")

if __name__ == "__main__":
    main() 