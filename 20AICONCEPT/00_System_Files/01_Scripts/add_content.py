#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

def create_basic_files(folder_path, topic):
    """Tạo các file cơ bản cho một thư mục"""
    
    # Tạo THEORY.md
    theory_content = f"""# 📚 Lý Thuyết - {topic}

## 🎯 Tổng Quan
{topic} là một khái niệm quan trọng trong AI/ML.

## 📖 Khái Niệm Cơ Bản
- Định nghĩa và nguyên lý
- Ứng dụng thực tế
- Ưu điểm và nhược điểm

## 🔬 Lý Thuyết Nâng Cao
- Mathematical foundation
- Algorithmic complexity
- Optimization techniques

## 📚 Tài Liệu Tham Khảo
1. Book 1: Author - Title
2. Paper 1: Author - Title
3. Research 1: Author - Title
"""
    
    # Tạo IMPLEMENTATION.md
    impl_content = f"""# 🛠️ Implementation - {topic}

## 🎯 Tổng Quan
Hướng dẫn implement {topic.lower()}.

## 📋 Prerequisites
- Python programming
- Basic mathematics
- Data structures

## 🚀 Basic Implementation
```python
import numpy as np
import pandas as pd

def basic_{topic.lower().replace(' ', '_')}(X, y):
    # Implementation here
    pass
```

## 🔧 Advanced Implementation
- Optimization techniques
- Error handling
- Performance tuning

## 📊 Evaluation
- Metrics calculation
- Visualization
- Performance analysis
"""
    
    # Tạo requirements.txt
    req_content = """numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
"""
    
    # Tạo files
    files_to_create = [
        ("THEORY.md", theory_content),
        ("IMPLEMENTATION.md", impl_content),
        ("requirements.txt", req_content)
    ]
    
    for filename, content in files_to_create:
        file_path = Path(folder_path) / filename
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Created: {file_path}")
        except Exception as e:
            print(f"❌ Error creating {file_path}: {e}")

def main():
    print("🚀 Bắt đầu tạo nội dung cơ bản...")
    
    # Tạo cho các thư mục chính
    main_folders = [
        ("01_Machine_Learning", "Machine Learning"),
        ("02_Deep_Learning", "Deep Learning"),
        ("03_Neural_Networks", "Neural Networks"),
        ("04_Natural_Language_Processing", "Natural Language Processing"),
        ("05_Computer_Vision", "Computer Vision"),
        ("06_Reinforcement_Learning", "Reinforcement Learning"),
        ("07_Generative_Models", "Generative Models"),
        ("08_Large_Language_Models", "Large Language Models"),
        ("09_Transformers", "Transformers"),
        ("10_Feature_Engineering", "Feature Engineering"),
        ("11_Supervised_Learning", "Supervised Learning"),
        ("12_Bayesian_Learning", "Bayesian Learning"),
        ("13_Prompt_Engineering", "Prompt Engineering"),
        ("14_AI_Agents", "AI Agents"),
        ("15_Fine_tuning_Models", "Fine-tuning Models"),
        ("16_Multimodal_Models", "Multimodal Models"),
        ("17_Embeddings", "Embeddings"),
        ("18_Vector_Search", "Vector Search"),
        ("19_Model_Evaluation", "Model Evaluation"),
        ("20_AI_Infrastructure", "AI Infrastructure")
    ]
    
    for folder_path, topic in main_folders:
        create_basic_files(folder_path, topic)
    
    print("🎉 Hoàn thành tạo nội dung cơ bản!")

if __name__ == "__main__":
    main() 