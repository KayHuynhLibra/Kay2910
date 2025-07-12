#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo 5 bài toán phức tạp cho tất cả thư mục con còn lại
"""

import os
from pathlib import Path

def create_generic_problems_file(folder_path, topic, category):
    """Tạo file COMPLEX_PROBLEMS.md generic cho các thư mục"""
    
    content = f"""# 🎯 5 Bài Toán Phức Tạp - {topic}

## 📊 Bài Toán 1: {category}_Advanced_Problem_1

### 🎯 Mô Tả
Xây dựng hệ thống {topic.lower()} với dữ liệu đa chiều và yêu cầu kỹ thuật nâng cao

### 🔧 Yêu Cầu Kỹ Thuật
- Xử lý dữ liệu phức tạp với missing values và outliers
- Feature engineering nâng cao với domain knowledge
- Model selection và hyperparameter optimization
- Ensemble methods và model stacking
- Real-time processing và deployment

### 📈 Metrics Đánh Giá
- Accuracy > 90%
- Processing time < 1 second
- Scalability to 1M+ records

---

## 🏥 Bài Toán 2: {category}_Real_World_Problem_2

### 🎯 Mô Tả
Ứng dụng {topic.lower()} trong môi trường thực tế với constraints nghiêm ngặt

### 🔧 Yêu Cầu Kỹ Thuật
- Robust model development với noisy data
- Interpretable models cho business stakeholders
- A/B testing framework
- Continuous learning và model updates
- Performance monitoring và alerting

### 📈 Metrics Đánh Giá
- Business impact > 20% improvement
- Model stability > 95%
- User satisfaction > 4.5/5

---

## 📈 Bài Toán 3: {category}_Research_Problem_3

### 🎯 Mô Tả
Nghiên cứu và phát triển novel approaches trong {topic.lower()}

### 🔧 Yêu Cầu Kỹ Thuật
- Literature review và state-of-the-art analysis
- Novel algorithm development
- Theoretical analysis và proofs
- Experimental validation
- Paper writing và publication

### 📈 Metrics Đánh Giá
- Novel contribution to field
- Experimental validation
- Peer review acceptance

---

## 🌍 Bài Toán 4: {category}_Production_Problem_4

### 🎯 Mô Tả
Triển khai {topic.lower()} trong production environment

### 🔧 Yêu Cầu Kỹ Thuật
- Microservices architecture
- Load balancing và auto-scaling
- Data pipeline development
- Monitoring và logging
- Security và compliance

### 📈 Metrics Đánh Giá
- 99.9% uptime
- Response time < 100ms
- Security compliance 100%

---

## 🚗 Bài Toán 5: {category}_Innovation_Problem_5

### 🎯 Mô Tả
Đổi mới sáng tạo trong {topic.lower()} với cutting-edge technologies

### 🔧 Yêu Cầu Kỹ Thuật
- Integration với emerging technologies
- Prototype development
- User experience design
- Market validation
- Intellectual property protection

### 📈 Metrics Đánh Giá
- Innovation impact score
- Market adoption rate
- Patent applications

---

## 🛠️ Công Cụ & Framework

### Python Libraries
```python
import pandas as pd
import numpy as np
import torch
import tensorflow as tf
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
```

### Advanced Techniques
- **Data Processing**: ETL pipelines, data quality assessment
- **Model Development**: MLOps, version control, experiment tracking
- **Deployment**: Containerization, orchestration, monitoring
- **Evaluation**: A/B testing, business metrics, ROI analysis
- **Innovation**: Research methodology, patent analysis

### Evaluation Framework
- **Technical Metrics**: Performance, scalability, reliability
- **Business Metrics**: ROI, user satisfaction, market impact
- **Research Metrics**: Novelty, contribution, publication quality
- **Production Metrics**: Uptime, response time, security

---

## 📚 Tài Liệu Tham Khảo

1. **Research Papers**: Latest publications in {topic}
2. **Industry Reports**: Market analysis và trends
3. **Technical Documentation**: Framework guides và best practices
4. **Case Studies**: Real-world implementations
5. **Innovation Resources**: Patent databases, research institutions

---

**Lưu ý**: Các bài toán này được thiết kế để thách thức ngay cả những người có kinh nghiệm. Hãy bắt đầu với từng phần nhỏ và dần dần mở rộng độ phức tạp.
"""
    
    file_path = Path(folder_path) / "COMPLEX_PROBLEMS.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {file_path}")

def get_all_subdirectories():
    """Lấy tất cả thư mục con trong cấu trúc AI/ML"""
    subdirs = []
    
    # Duyệt qua tất cả thư mục
    for root, dirs, files in os.walk('.'):
        # Bỏ qua thư mục gốc và các thư mục ẩn
        if root == '.' or any(part.startswith('.') for part in Path(root).parts):
            continue
            
        # Chỉ lấy thư mục con (không phải thư mục gốc)
        if len(Path(root).parts) > 1:
            for dir_name in dirs:
                full_path = Path(root) / dir_name
                # Tạo tên topic từ tên thư mục
                topic = dir_name.replace('_', ' ').title()
                # Tạo category từ tên thư mục
                category = ''.join([word[0] for word in dir_name.split('_')])
                
                subdirs.append((str(full_path), topic, category))
    
    return subdirs

def main():
    """Main function để tạo bài toán cho tất cả thư mục con"""
    
    print("🚀 Bắt đầu tạo 5 bài toán phức tạp cho tất cả thư mục con...")
    
    # Lấy tất cả thư mục con
    subdirs = get_all_subdirectories()
    
    # Lọc ra các thư mục chưa có file COMPLEX_PROBLEMS.md
    existing_files = set()
    for root, dirs, files in os.walk('.'):
        if 'COMPLEX_PROBLEMS.md' in files:
            existing_files.add(Path(root))
    
    # Tạo bài toán cho các thư mục chưa có
    created_count = 0
    for folder_path, topic, category in subdirs:
        folder_path_obj = Path(folder_path)
        if folder_path_obj not in existing_files:
            create_generic_problems_file(folder_path, topic, category)
            created_count += 1
    
    print(f"\n🎉 Hoàn thành! Đã tạo thêm {created_count} file COMPLEX_PROBLEMS.md")
    print(f"📝 Tổng cộng: {len(subdirs)} thư mục con đã có bài toán phức tạp")
    
    # Thống kê theo level
    level_stats = {}
    for folder_path, topic, category in subdirs:
        level = folder_path.split('\\')[0] if '\\' in folder_path else folder_path.split('/')[0]
        if level not in level_stats:
            level_stats[level] = 0
        level_stats[level] += 1
    
    print("\n📊 Thống kê theo level:")
    for level, count in sorted(level_stats.items()):
        print(f"   {level}: {count} thư mục con")

if __name__ == "__main__":
    main() 