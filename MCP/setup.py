#!/usr/bin/env python3
"""
Setup script cho AI 2025 với MCP
Tự động cài đặt và cấu hình môi trường học tập
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    """In banner chào mừng"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  🚀 AI 2025 với MCP - Khóa học toàn diện                    ║
    ║                                                              ║
    ║  Model Context Protocol + Advanced AI Training              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Kiểm tra phiên bản Python"""
    print("🐍 Kiểm tra phiên bản Python...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Yêu cầu Python 3.9 hoặc cao hơn!")
        print(f"   Phiên bản hiện tại: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def check_system_requirements():
    """Kiểm tra yêu cầu hệ thống"""
    print("\n💻 Kiểm tra yêu cầu hệ thống...")
    
    # Kiểm tra RAM
    try:
        import psutil
        ram_gb = psutil.virtual_memory().total / (1024**3)
        print(f"   RAM: {ram_gb:.1f} GB")
        if ram_gb < 8:
            print("⚠️  Khuyến nghị ít nhất 8GB RAM")
        else:
            print("✅ RAM - OK")
    except ImportError:
        print("⚠️  Không thể kiểm tra RAM (cần psutil)")
    
    # Kiểm tra GPU
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            print(f"✅ GPU: {gpu_name} - CUDA available")
        else:
            print("⚠️  GPU không có CUDA - Training sẽ chậm")
    except ImportError:
        print("⚠️  PyTorch chưa được cài đặt")
    
    # Kiểm tra OS
    os_name = platform.system()
    print(f"   OS: {os_name} {platform.release()}")
    
    return True

def install_dependencies():
    """Cài đặt dependencies"""
    print("\n📦 Cài đặt dependencies...")
    
    try:
        # Upgrade pip
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        print("✅ Pip upgraded")
        
        # Install requirements
        if os.path.exists("requirements.txt"):
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                          check=True)
            print("✅ Dependencies installed")
        else:
            print("❌ requirements.txt không tìm thấy")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi cài đặt: {e}")
        return False
    
    return True

def create_directories():
    """Tạo thư mục cần thiết"""
    print("\n📁 Tạo thư mục...")
    
    directories = [
        "data",
        "models",
        "logs",
        "checkpoints",
        "experiments",
        "datasets",
        "outputs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created: {directory}/")

def download_sample_data():
    """Tải dữ liệu mẫu"""
    print("\n📊 Tải dữ liệu mẫu...")
    
    # Tạo file dữ liệu mẫu
    sample_data = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
        ],
        "products": [
            {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
            {"id": 2, "name": "Mouse", "price": 29.99, "category": "Electronics"},
            {"id": 3, "name": "Book", "price": 19.99, "category": "Education"}
        ],
        "orders": [
            {"id": 1, "user_id": 1, "product_id": 1, "quantity": 1, "total": 999.99},
            {"id": 2, "user_id": 2, "product_id": 2, "quantity": 2, "total": 59.98},
            {"id": 3, "user_id": 3, "product_id": 3, "quantity": 1, "total": 19.99}
        ]
    }
    
    import json
    with open("data/sample_data.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    
    print("✅ Sample data created: data/sample_data.json")

def run_tests():
    """Chạy tests cơ bản"""
    print("\n🧪 Chạy tests...")
    
    try:
        # Test MCP basics
        result = subprocess.run([sys.executable, "code/01_mcp_basics.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ MCP basics test - PASSED")
        else:
            print("❌ MCP basics test - FAILED")
            print(f"Error: {result.stderr}")
        
        # Test AI training examples
        result = subprocess.run([sys.executable, "code/02_ai_training_examples.py"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✅ AI training examples test - PASSED")
        else:
            print("❌ AI training examples test - FAILED")
            print(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("⚠️  Tests timed out (this is normal for first run)")
    except Exception as e:
        print(f"⚠️  Test error: {e}")

def create_config():
    """Tạo file cấu hình"""
    print("\n⚙️ Tạo file cấu hình...")
    
    config = {
        "project_name": "AI 2025 với MCP",
        "version": "1.0.0",
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "data_path": "./data",
        "models_path": "./models",
        "logs_path": "./logs",
        "checkpoints_path": "./checkpoints",
        "experiments_path": "./experiments",
        "outputs_path": "./outputs",
        "settings": {
            "default_model": "gpt2",
            "batch_size": 4,
            "learning_rate": 5e-5,
            "max_length": 512,
            "num_epochs": 3
        }
    }
    
    import json
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("✅ Configuration created: config.json")

def print_next_steps():
    """In hướng dẫn tiếp theo"""
    print("\n" + "="*60)
    print("🎉 Cài đặt hoàn thành!")
    print("="*60)
    
    print("\n📚 Bước tiếp theo:")
    print("1. 📖 Đọc: theory/01_mcp_introduction.md")
    print("2. 🎓 Làm theo: tutorials/01_introduction.md")
    print("3. 💻 Chạy: python code/01_mcp_basics.py")
    print("4. 🧠 Thực hành: python code/02_ai_training_examples.py")
    print("5. 🚀 Khám phá: python code/03_advanced_ai_2025.py")
    
    print("\n🔗 Tài nguyên:")
    print("- 📖 Lý thuyết: theory/")
    print("- 💻 Code mẫu: code/")
    print("- 🎓 Hướng dẫn: tutorials/")
    print("- 📚 Tài nguyên: resources/")
    
    print("\n💡 Tips:")
    print("- Sử dụng Jupyter Notebook để thực hành")
    print("- Tham gia Discord community để hỗ trợ")
    print("- Tạo dự án riêng để áp dụng kiến thức")
    print("- Cập nhật thường xuyên với AI trends mới")
    
    print("\n🚀 Chúc bạn thành công trên hành trình AI 2025!")
    print("="*60)

def main():
    """Hàm chính"""
    print_banner()
    
    # Kiểm tra Python version
    if not check_python_version():
        sys.exit(1)
    
    # Kiểm tra system requirements
    check_system_requirements()
    
    # Cài đặt dependencies
    if not install_dependencies():
        print("❌ Lỗi cài đặt dependencies")
        sys.exit(1)
    
    # Tạo thư mục
    create_directories()
    
    # Tải dữ liệu mẫu
    download_sample_data()
    
    # Tạo cấu hình
    create_config()
    
    # Chạy tests
    run_tests()
    
    # In hướng dẫn tiếp theo
    print_next_steps()

if __name__ == "__main__":
    main() 