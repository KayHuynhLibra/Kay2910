#!/usr/bin/env python3
"""
Create Sample Data - Tạo dữ liệu mẫu thực tế cho dự án AI 2025 với MCP
"""

import os
import json
import numpy as np
import torch
import pandas as pd
from datetime import datetime
import cv2
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import seaborn as sns

def create_directories():
    """Tạo các thư mục cần thiết"""
    directories = [
        'data/raw',
        'data/processed', 
        'data/samples',
        'datasets/text',
        'datasets/images',
        'datasets/numerical',
        'models/checkpoints',
        'models/saved',
        'logs/training',
        'logs/evaluation',
        'outputs/plots',
        'outputs/results',
        'experiments/configs',
        'experiments/results'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created: {directory}")

def create_text_data():
    """Tạo dữ liệu text mẫu"""
    print("\n=== Tạo dữ liệu text ===")
    
    # Dữ liệu văn bản đa dạng
    text_samples = {
        'sentiment': [
            "Tôi rất hài lòng với sản phẩm này!",
            "Chất lượng không tốt như mong đợi.",
            "Dịch vụ khách hàng tuyệt vời!",
            "Giá cả hợp lý và chất lượng tốt.",
            "Không nên mua sản phẩm này.",
            "Rất thích cách thiết kế của sản phẩm.",
            "Giao hàng chậm và không đúng hẹn.",
            "Sản phẩm đúng như mô tả, rất hài lòng!"
        ],
        'news': [
            "AI đang thay đổi cách chúng ta làm việc trong năm 2025.",
            "Công nghệ blockchain được ứng dụng rộng rãi trong tài chính.",
            "Việt Nam đạt được nhiều thành tựu trong lĩnh vực công nghệ.",
            "Biến đổi khí hậu ảnh hưởng nghiêm trọng đến nông nghiệp.",
            "Giáo dục trực tuyến trở thành xu hướng chính sau đại dịch.",
            "Thành phố thông minh đang được phát triển tại nhiều nơi.",
            "Y tế số giúp cải thiện chất lượng chăm sóc sức khỏe.",
            "Năng lượng tái tạo chiếm ưu thế trong tương lai."
        ],
        'technical': [
            "Transformer architecture revolutionized natural language processing.",
            "Deep learning models require large amounts of training data.",
            "Federated learning enables privacy-preserving machine learning.",
            "Multimodal AI combines text, image, and audio processing.",
            "Edge computing reduces latency for real-time applications.",
            "Quantum computing shows promise for complex optimization problems.",
            "Computer vision algorithms can detect objects in real-time.",
            "Reinforcement learning is used in autonomous systems."
        ]
    }
    
    # Lưu vào file
    for category, texts in text_samples.items():
        filename = f'datasets/text/{category}_data.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'category': category,
                'samples': texts,
                'created_at': datetime.now().isoformat(),
                'total_samples': len(texts)
            }, f, ensure_ascii=False, indent=2)
        print(f"Created: {filename} ({len(texts)} samples)")
    
    # Tạo file tổng hợp
    all_texts = []
    for texts in text_samples.values():
        all_texts.extend(texts)
    
    with open('datasets/text/all_text_data.json', 'w', encoding='utf-8') as f:
        json.dump({
            'all_samples': all_texts,
            'created_at': datetime.now().isoformat(),
            'total_samples': len(all_texts)
        }, f, ensure_ascii=False, indent=2)
    print(f"Created: datasets/text/all_text_data.json ({len(all_texts)} samples)")

def create_image_data():
    """Tạo dữ liệu ảnh mẫu"""
    print("\n=== Tạo dữ liệu ảnh ===")
    
    # Tạo ảnh mẫu với các hình dạng khác nhau
    image_categories = {
        'shapes': ['circle', 'square', 'triangle', 'rectangle'],
        'colors': ['red', 'green', 'blue', 'yellow'],
        'patterns': ['stripes', 'dots', 'solid', 'gradient']
    }
    
    for category, items in image_categories.items():
        os.makedirs(f'datasets/images/{category}', exist_ok=True)
        
        for i, item in enumerate(items):
            # Tạo ảnh 224x224 với màu sắc khác nhau
            img = Image.new('RGB', (224, 224), color='white')
            draw = ImageDraw.Draw(img)
            
            # Vẽ hình dạng khác nhau
            if category == 'shapes':
                if item == 'circle':
                    draw.ellipse([50, 50, 174, 174], fill='red', outline='black', width=3)
                elif item == 'square':
                    draw.rectangle([50, 50, 174, 174], fill='blue', outline='black', width=3)
                elif item == 'triangle':
                    draw.polygon([(112, 50), (50, 174), (174, 174)], fill='green', outline='black', width=3)
                elif item == 'rectangle':
                    draw.rectangle([30, 80, 194, 144], fill='yellow', outline='black', width=3)
            
            # Lưu ảnh
            filename = f'datasets/images/{category}/{item}.png'
            img.save(filename)
            print(f"Created: {filename}")
    
    # Tạo metadata
    metadata = {
        'categories': image_categories,
        'image_size': (224, 224),
        'format': 'PNG',
        'created_at': datetime.now().isoformat()
    }
    
    with open('datasets/images/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    print("Created: datasets/images/metadata.json")

def create_numerical_data():
    """Tạo dữ liệu số mẫu"""
    print("\n=== Tạo dữ liệu số ===")
    
    # Tạo dữ liệu với các phân phối khác nhau
    np.random.seed(42)  # Để kết quả có thể tái tạo
    
    datasets = {
        'sales_data': {
            'data': np.random.normal(1000, 200, (1000, 5)),  # Doanh số
            'columns': ['product_id', 'quantity', 'price', 'customer_id', 'date_code']
        },
        'user_behavior': {
            'data': np.random.exponential(2, (500, 4)),  # Thời gian sử dụng
            'columns': ['session_duration', 'page_views', 'clicks', 'bounce_rate']
        },
        'sensor_data': {
            'data': np.random.uniform(20, 30, (800, 6)),  # Dữ liệu cảm biến
            'columns': ['temperature', 'humidity', 'pressure', 'light', 'noise', 'motion']
        },
        'financial_data': {
            'data': np.random.lognormal(0, 1, (600, 4)),  # Dữ liệu tài chính
            'columns': ['stock_price', 'volume', 'market_cap', 'pe_ratio']
        }
    }
    
    for name, dataset in datasets.items():
        # Tạo DataFrame
        df = pd.DataFrame(dataset['data'], columns=dataset['columns'])
        
        # Thêm ID
        df.insert(0, 'id', range(1, len(df) + 1))
        
        # Lưu CSV
        csv_filename = f'datasets/numerical/{name}.csv'
        df.to_csv(csv_filename, index=False)
        print(f"Created: {csv_filename} ({len(df)} rows, {len(df.columns)} columns)")
        
        # Lưu JSON
        json_filename = f'datasets/numerical/{name}.json'
        with open(json_filename, 'w') as f:
            json.dump({
                'name': name,
                'data': df.to_dict('records'),
                'statistics': {
                    'mean': df.mean().to_dict(),
                    'std': df.std().to_dict(),
                    'min': df.min().to_dict(),
                    'max': df.max().to_dict()
                },
                'created_at': datetime.now().isoformat()
            }, f, indent=2)
        print(f"Created: {json_filename}")
    
    # Tạo file tổng hợp
    all_data = {}
    for name, dataset in datasets.items():
        all_data[name] = {
            'shape': dataset['data'].shape,
            'columns': dataset['columns'],
            'mean': dataset['data'].mean(axis=0).tolist(),
            'std': dataset['data'].std(axis=0).tolist()
        }
    
    with open('datasets/numerical/summary.json', 'w') as f:
        json.dump({
            'datasets': all_data,
            'total_datasets': len(datasets),
            'created_at': datetime.now().isoformat()
        }, f, indent=2)
    print("Created: datasets/numerical/summary.json")

def create_config_files():
    """Tạo file cấu hình cho các thí nghiệm"""
    print("\n=== Tạo file cấu hình ===")
    
    configs = {
        'mcp_config.json': {
            'server': {
                'host': 'localhost',
                'port': 8000,
                'max_connections': 10
            },
            'resources': {
                'database': 'sqlite:///data/samples/sample.db',
                'filesystem': './data/samples',
                'api_endpoint': 'https://api.example.com'
            },
            'tools': {
                'data_analysis': True,
                'file_processor': True,
                'model_training': True
            }
        },
        'training_config.json': {
            'model': {
                'type': 'transformer',
                'hidden_size': 768,
                'num_layers': 12,
                'num_heads': 12
            },
            'training': {
                'batch_size': 32,
                'learning_rate': 1e-4,
                'num_epochs': 100,
                'warmup_steps': 1000
            },
            'data': {
                'train_split': 0.8,
                'val_split': 0.1,
                'test_split': 0.1,
                'max_length': 512
            }
        },
        'multimodal_config.json': {
            'text_encoder': {
                'model_name': 'bert-base-uncased',
                'max_length': 512,
                'hidden_size': 768
            },
            'image_encoder': {
                'model_name': 'resnet50',
                'input_size': 224,
                'hidden_size': 512
            },
            'fusion': {
                'method': 'attention',
                'hidden_size': 1024,
                'dropout': 0.1
            }
        }
    }
    
    for filename, config in configs.items():
        filepath = f'experiments/configs/{filename}'
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Created: {filepath}")

def create_sample_plots():
    """Tạo các biểu đồ mẫu"""
    print("\n=== Tạo biểu đồ mẫu ===")
    
    # Tạo dữ liệu cho biểu đồ
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.exp(-x/3)
    
    # 1. Line plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', linewidth=2)
    plt.plot(x, y2, label='cos(x)', linewidth=2)
    plt.plot(x, y3, label='exp(-x/3)', linewidth=2)
    plt.title('Sample Mathematical Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/plots/mathematical_functions.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created: outputs/plots/mathematical_functions.png")
    
    # 2. Scatter plot
    np.random.seed(42)
    x_scatter = np.random.normal(0, 1, 100)
    y_scatter = 2 * x_scatter + np.random.normal(0, 0.5, 100)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_scatter, y_scatter, alpha=0.6, color='blue')
    plt.title('Sample Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/plots/scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created: outputs/plots/scatter_plot.png")
    
    # 3. Histogram
    data_hist = np.random.normal(0, 1, 1000)
    
    plt.figure(figsize=(8, 6))
    plt.hist(data_hist, bins=30, alpha=0.7, color='green', edgecolor='black')
    plt.title('Sample Histogram (Normal Distribution)')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/plots/histogram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created: outputs/plots/histogram.png")

def create_log_files():
    """Tạo file log mẫu"""
    print("\n=== Tạo file log mẫu ===")
    
    # Training log
    training_log = """2025-01-15 10:00:00 - INFO - Starting training session
2025-01-15 10:00:05 - INFO - Loading dataset: 1000 samples
2025-01-15 10:00:10 - INFO - Model initialized with 1.2M parameters
2025-01-15 10:01:00 - INFO - Epoch 1/100 - Loss: 2.3456 - Accuracy: 0.2345
2025-01-15 10:02:00 - INFO - Epoch 2/100 - Loss: 1.9876 - Accuracy: 0.3456
2025-01-15 10:03:00 - INFO - Epoch 3/100 - Loss: 1.6543 - Accuracy: 0.4567
2025-01-15 10:04:00 - INFO - Epoch 4/100 - Loss: 1.4321 - Accuracy: 0.5678
2025-01-15 10:05:00 - INFO - Epoch 5/100 - Loss: 1.2345 - Accuracy: 0.6789
"""
    
    with open('logs/training/sample_training.log', 'w') as f:
        f.write(training_log)
    print("Created: logs/training/sample_training.log")
    
    # Evaluation log
    eval_log = """2025-01-15 11:00:00 - INFO - Starting evaluation
2025-01-15 11:00:05 - INFO - Loading test dataset: 200 samples
2025-01-15 11:00:10 - INFO - Running inference...
2025-01-15 11:00:30 - INFO - Evaluation completed
2025-01-15 11:00:30 - INFO - Test Accuracy: 0.8234
2025-01-15 11:00:30 - INFO - Test Loss: 0.4567
2025-01-15 11:00:30 - INFO - Precision: 0.8123
2025-01-15 11:00:30 - INFO - Recall: 0.7890
2025-01-15 11:00:30 - INFO - F1-Score: 0.8005
"""
    
    with open('logs/evaluation/sample_evaluation.log', 'w') as f:
        f.write(eval_log)
    print("Created: logs/evaluation/sample_evaluation.log")

def main():
    """Hàm chính để tạo tất cả dữ liệu mẫu"""
    print("=== Tạo dữ liệu mẫu cho dự án AI 2025 với MCP ===")
    print("=" * 60)
    
    # Tạo thư mục
    create_directories()
    
    # Tạo dữ liệu
    create_text_data()
    create_image_data()
    create_numerical_data()
    
    # Tạo file cấu hình
    create_config_files()
    
    # Tạo biểu đồ mẫu
    create_sample_plots()
    
    # Tạo file log
    create_log_files()
    
    print("\n" + "=" * 60)
    print("✅ Hoàn thành tạo dữ liệu mẫu!")
    print("\n📁 Cấu trúc dữ liệu đã tạo:")
    print("├── data/")
    print("│   ├── raw/")
    print("│   ├── processed/")
    print("│   └── samples/")
    print("├── datasets/")
    print("│   ├── text/ (24 samples)")
    print("│   ├── images/ (16 images)")
    print("│   └── numerical/ (4 datasets)")
    print("├── models/")
    print("│   ├── checkpoints/")
    print("│   └── saved/")
    print("├── logs/")
    print("│   ├── training/")
    print("│   └── evaluation/")
    print("├── outputs/")
    print("│   ├── plots/ (3 plots)")
    print("│   └── results/")
    print("└── experiments/")
    print("    ├── configs/ (3 configs)")
    print("    └── results/")
    
    print("\n🚀 Bạn có thể bắt đầu thử nghiệm với dữ liệu này!")

if __name__ == "__main__":
    main() 