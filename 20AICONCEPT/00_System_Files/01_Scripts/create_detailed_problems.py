#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo 5 bài toán phức tạp chi tiết cho tất cả thư mục AI/ML
"""

import os
import json
from pathlib import Path

# Định nghĩa các bài toán phức tạp cho từng loại thư mục
COMPLEX_PROBLEMS = {
    "Machine_Learning": {
        "problems": [
            {
                "title": "Dự Đoán Giá Nhà Đa Biến với Feature Engineering Nâng Cao",
                "description": "Xây dựng mô hình dự đoán giá nhà sử dụng 50+ features bao gồm đặc điểm địa lý, kinh tế, môi trường, xã hội",
                "techniques": [
                    "Xử lý missing data với multiple imputation",
                    "Feature engineering: tạo interaction terms, polynomial features",
                    "Regularization: Ridge, Lasso, Elastic Net",
                    "Cross-validation với time series split",
                    "Ensemble methods: Stacking với Random Forest, XGBoost"
                ],
                "metrics": [
                    "RMSE < 15% của giá trung bình",
                    "R² > 0.85",
                    "MAPE < 10%"
                ]
            },
            {
                "title": "Dự Đoán Tuổi Thọ Bệnh Nhân với Dữ Liệu Y Tế Đa Chiều",
                "description": "Phân tích dự đoán tuổi thọ dựa trên 100+ biomarkers, lịch sử bệnh án, thông tin lối sống",
                "techniques": [
                    "Feature selection với recursive feature elimination",
                    "Handling multicollinearity với VIF analysis",
                    "Robust regression với Huber loss",
                    "Bayesian linear regression",
                    "Uncertainty quantification"
                ],
                "metrics": [
                    "MAE < 2 năm",
                    "Confidence interval coverage > 90%",
                    "Calibration error < 0.05"
                ]
            },
            {
                "title": "Dự Đoán Giá Cổ Phiếu với Dữ Liệu Thời Gian Thực",
                "description": "Dự đoán giá cổ phiếu trong 24h tới sử dụng dữ liệu giá lịch sử, technical indicators, sentiment analysis",
                "techniques": [
                    "Time series feature engineering",
                    "Handling non-stationarity",
                    "Multiple regression với lagged variables",
                    "Online learning với concept drift detection",
                    "Risk-adjusted return optimization"
                ],
                "metrics": [
                    "Directional accuracy > 60%",
                    "Sharpe ratio > 1.5",
                    "Maximum drawdown < 10%"
                ]
            },
            {
                "title": "Dự Đoán Biến Đổi Khí Hậu với Dữ Liệu Đa Nguồn",
                "description": "Dự đoán nhiệt độ trung bình toàn cầu sử dụng satellite data, ocean data, atmospheric data",
                "techniques": [
                    "Spatiotemporal regression",
                    "Handling autocorrelation",
                    "Seasonal decomposition",
                    "Long-term trend analysis",
                    "Uncertainty propagation"
                ],
                "metrics": [
                    "RMSE < 0.5°C",
                    "Trend accuracy > 90%",
                    "Long-term prediction stability"
                ]
            },
            {
                "title": "Dự Đoán Tiêu Thụ Nhiên Liệu Xe Hơi với IoT Data",
                "description": "Dự đoán mức tiêu thụ nhiên liệu dựa trên real-time sensor data, driving behavior, environmental conditions",
                "techniques": [
                    "Real-time feature engineering",
                    "Handling sensor noise và outliers",
                    "Adaptive learning với concept drift",
                    "Multi-objective optimization",
                    "Interpretable models"
                ],
                "metrics": [
                    "RMSE < 0.5 L/100km",
                    "Real-time prediction latency < 100ms",
                    "Model interpretability score > 0.8"
                ]
            }
        ]
    },
    "Deep_Learning": {
        "problems": [
            {
                "title": "Phân Loại Hình Ảnh Y Tế với Transfer Learning",
                "description": "Phân loại bệnh từ hình ảnh X-ray, MRI, CT scan sử dụng pre-trained models",
                "techniques": [
                    "Transfer learning với ImageNet pre-trained models",
                    "Data augmentation với medical imaging",
                    "Attention mechanisms",
                    "Multi-task learning",
                    "Explainable AI techniques"
                ],
                "metrics": [
                    "Accuracy > 95%",
                    "Sensitivity > 90%",
                    "Specificity > 95%"
                ]
            },
            {
                "title": "Dịch Máy Neural với Attention",
                "description": "Xây dựng hệ thống dịch máy đa ngôn ngữ với attention mechanism",
                "techniques": [
                    "Sequence-to-sequence models",
                    "Attention mechanisms",
                    "Beam search decoding",
                    "Subword tokenization",
                    "Multi-language training"
                ],
                "metrics": [
                    "BLEU score > 30",
                    "Translation speed < 1s per sentence",
                    "Memory usage < 8GB"
                ]
            },
            {
                "title": "Tạo Hình Ảnh với GANs",
                "description": "Tạo hình ảnh thực tế từ text descriptions sử dụng GANs",
                "techniques": [
                    "Conditional GANs",
                    "Progressive growing",
                    "Style transfer",
                    "Adversarial training",
                    "Quality assessment"
                ],
                "metrics": [
                    "FID score < 20",
                    "Inception score > 8",
                    "Human evaluation score > 4/5"
                ]
            },
            {
                "title": "Reinforcement Learning cho Game AI",
                "description": "Xây dựng AI chơi game phức tạp với deep reinforcement learning",
                "techniques": [
                    "Deep Q-Networks",
                    "Policy gradient methods",
                    "Actor-critic algorithms",
                    "Experience replay",
                    "Curriculum learning"
                ],
                "metrics": [
                    "Win rate > 80%",
                    "Learning speed < 1000 episodes",
                    "Generalization to new levels"
                ]
            },
            {
                "title": "Time Series Forecasting với LSTM",
                "description": "Dự đoán chuỗi thời gian phức tạp với LSTM networks",
                "techniques": [
                    "Bidirectional LSTM",
                    "Attention mechanisms",
                    "Multi-step forecasting",
                    "Ensemble methods",
                    "Uncertainty quantification"
                ],
                "metrics": [
                    "RMSE < 10% of mean",
                    "Directional accuracy > 70%",
                    "Forecast horizon > 30 steps"
                ]
            }
        ]
    },
    "Natural_Language_Processing": {
        "problems": [
            {
                "title": "Question Answering với BERT",
                "description": "Xây dựng hệ thống trả lời câu hỏi từ văn bản sử dụng BERT",
                "techniques": [
                    "BERT fine-tuning",
                    "Span extraction",
                    "Multi-hop reasoning",
                    "Evidence selection",
                    "Answer validation"
                ],
                "metrics": [
                    "Exact match > 70%",
                    "F1 score > 75%",
                    "Response time < 2s"
                ]
            },
            {
                "title": "Sentiment Analysis với Aspect-based",
                "description": "Phân tích sentiment chi tiết cho từng aspect của sản phẩm/dịch vụ",
                "techniques": [
                    "Aspect extraction",
                    "Sentiment classification",
                    "Multi-aspect modeling",
                    "Context understanding",
                    "Cross-domain adaptation"
                ],
                "metrics": [
                    "Aspect accuracy > 85%",
                    "Sentiment accuracy > 90%",
                    "F1 score > 0.8"
                ]
            },
            {
                "title": "Text Summarization với Transformer",
                "description": "Tạo tóm tắt văn bản dài với transformer-based models",
                "techniques": [
                    "Extractive summarization",
                    "Abstractive summarization",
                    "Attention mechanisms",
                    "Length control",
                    "Factual consistency"
                ],
                "metrics": [
                    "ROUGE-L > 0.4",
                    "BLEU score > 0.3",
                    "Human evaluation > 4/5"
                ]
            },
            {
                "title": "Named Entity Recognition với BiLSTM-CRF",
                "description": "Nhận diện và phân loại entities trong văn bản",
                "techniques": [
                    "BiLSTM-CRF",
                    "Character-level embeddings",
                    "Contextual embeddings",
                    "Multi-task learning",
                    "Active learning"
                ],
                "metrics": [
                    "F1 score > 90%",
                    "Precision > 92%",
                    "Recall > 88%"
                ]
            },
            {
                "title": "Machine Translation với Transformer",
                "description": "Dịch máy chất lượng cao giữa nhiều ngôn ngữ",
                "techniques": [
                    "Transformer architecture",
                    "Multi-language training",
                    "Back-translation",
                    "Beam search",
                    "Quality estimation"
                ],
                "metrics": [
                    "BLEU score > 35",
                    "Translation speed < 0.5s",
                    "Memory efficiency < 4GB"
                ]
            }
        ]
    },
    "Computer_Vision": {
        "problems": [
            {
                "title": "Object Detection với YOLO",
                "description": "Phát hiện và định vị objects trong hình ảnh real-time",
                "techniques": [
                    "YOLO architecture",
                    "Multi-scale detection",
                    "Non-maximum suppression",
                    "Data augmentation",
                    "Model optimization"
                ],
                "metrics": [
                    "mAP > 0.8",
                    "FPS > 30",
                    "Accuracy > 85%"
                ]
            },
            {
                "title": "Image Segmentation với U-Net",
                "description": "Phân đoạn pixel-level cho medical imaging",
                "techniques": [
                    "U-Net architecture",
                    "Skip connections",
                    "Data augmentation",
                    "Loss functions",
                    "Post-processing"
                ],
                "metrics": [
                    "Dice coefficient > 0.9",
                    "IoU > 0.85",
                    "Processing time < 5s"
                ]
            },
            {
                "title": "Face Recognition với Deep Learning",
                "description": "Nhận diện khuôn mặt trong điều kiện thực tế",
                "techniques": [
                    "Face detection",
                    "Feature extraction",
                    "Face embedding",
                    "Similarity matching",
                    "Anti-spoofing"
                ],
                "metrics": [
                    "Accuracy > 99%",
                    "FAR < 0.001",
                    "FRR < 0.01"
                ]
            },
            {
                "title": "Video Analysis với 3D CNNs",
                "description": "Phân tích hành động và sự kiện trong video",
                "techniques": [
                    "3D convolutional networks",
                    "Temporal modeling",
                    "Action recognition",
                    "Video understanding",
                    "Real-time processing"
                ],
                "metrics": [
                    "Action accuracy > 90%",
                    "Processing speed > 25 FPS",
                    "Temporal localization accuracy > 80%"
                ]
            },
            {
                "title": "Image Generation với Style Transfer",
                "description": "Tạo hình ảnh nghệ thuật với style transfer",
                "techniques": [
                    "Neural style transfer",
                    "Content preservation",
                    "Style extraction",
                    "Multi-style synthesis",
                    "Real-time generation"
                ],
                "metrics": [
                    "Style similarity > 0.8",
                    "Content preservation > 0.9",
                    "Generation time < 10s"
                ]
            }
        ]
    }
}

def create_complex_problems_file(folder_path, topic, problems_data):
    """Tạo file COMPLEX_PROBLEMS.md cho một thư mục"""
    
    content = f"""# 🎯 5 Bài Toán Phức Tạp - {topic}

"""
    
    for i, problem in enumerate(problems_data["problems"], 1):
        content += f"""## 📊 Bài Toán {i}: {problem['title']}

### 🎯 Mô Tả
{problem['description']}

### 🔧 Yêu Cầu Kỹ Thuật
"""
        for technique in problem['techniques']:
            content += f"- {technique}\n"
        
        content += f"""
### 📈 Metrics Đánh Giá
"""
        for metric in problem['metrics']:
            content += f"- {metric}\n"
        
        content += "\n---\n\n"
    
    content += """## 🛠️ Công Cụ & Framework

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
- **Deep Learning**: Neural networks, CNNs, RNNs, Transformers
- **Machine Learning**: Ensemble methods, feature engineering, hyperparameter tuning
- **Data Processing**: Data augmentation, normalization, handling missing data
- **Evaluation**: Cross-validation, metrics analysis, model interpretation
- **Deployment**: Model serving, API development, monitoring

### Evaluation Framework
- **Cross-validation**: Stratified k-fold, time series split
- **Metrics**: Accuracy, precision, recall, F1-score, AUC-ROC
- **Diagnostics**: Confusion matrix, learning curves, feature importance
- **Business Impact**: ROI calculation, cost-benefit analysis

---

## 📚 Tài Liệu Tham Khảo

1. **Deep Learning**: "Deep Learning" - Ian Goodfellow, Yoshua Bengio, Aaron Courville
2. **Machine Learning**: "Pattern Recognition and Machine Learning" - Christopher Bishop
3. **Computer Vision**: "Computer Vision: Algorithms and Applications" - Richard Szeliski
4. **NLP**: "Speech and Language Processing" - Dan Jurafsky, James H. Martin
5. **Practical ML**: "Hands-On Machine Learning" - Aurélien Géron

---

**Lưu ý**: Các bài toán này được thiết kế để thách thức ngay cả những người có kinh nghiệm. Hãy bắt đầu với từng phần nhỏ và dần dần mở rộng độ phức tạp.
"""
    
    file_path = Path(folder_path) / "COMPLEX_PROBLEMS.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {file_path}")

def create_generic_problems_file(folder_path, topic, category):
    """Tạo file COMPLEX_PROBLEMS.md generic cho các thư mục khác"""
    
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

def main():
    """Main function để tạo tất cả bài toán phức tạp"""
    
    print("🚀 Bắt đầu tạo 5 bài toán phức tạp cho tất cả thư mục...")
    
    # Tạo cho các thư mục chính
    main_folders = [
        ("01_Machine_Learning", "Machine Learning", "ML"),
        ("02_Deep_Learning", "Deep Learning", "DL"),
        ("03_Neural_Networks", "Neural Networks", "NN"),
        ("04_Natural_Language_Processing", "Natural Language Processing", "NLP"),
        ("05_Computer_Vision", "Computer Vision", "CV"),
        ("06_Reinforcement_Learning", "Reinforcement Learning", "RL"),
        ("07_Generative_Models", "Generative Models", "GM"),
        ("08_Large_Language_Models", "Large Language Models", "LLM"),
        ("09_Transformers", "Transformers", "TR"),
        ("10_Feature_Engineering", "Feature Engineering", "FE"),
        ("11_Supervised_Learning", "Supervised Learning", "SL"),
        ("12_Bayesian_Learning", "Bayesian Learning", "BL"),
        ("13_Prompt_Engineering", "Prompt Engineering", "PE"),
        ("14_AI_Agents", "AI Agents", "AA"),
        ("15_Fine_tuning_Models", "Fine-tuning Models", "FT"),
        ("16_Multimodal_Models", "Multimodal Models", "MM"),
        ("17_Embeddings", "Embeddings", "EM"),
        ("18_Vector_Search", "Vector Search", "VS"),
        ("19_Model_Evaluation", "Model Evaluation", "ME"),
        ("20_AI_Infrastructure", "AI Infrastructure", "AI")
    ]
    
    # Tạo cho các thư mục có dữ liệu chi tiết
    for folder_path, topic, category in main_folders:
        if topic.replace(" ", "_") in COMPLEX_PROBLEMS:
            create_complex_problems_file(folder_path, topic, COMPLEX_PROBLEMS[topic.replace(" ", "_")])
        else:
            create_generic_problems_file(folder_path, topic, category)
    
    # Tạo cho các thư mục con quan trọng
    sub_folders = [
        # Machine Learning sub-folders
        ("01_Machine_Learning/01_Algorithms", "Machine Learning Algorithms", "MLA"),
        ("01_Machine_Learning/02_Statistics", "Statistical Analysis", "STAT"),
        ("01_Machine_Learning/03_Model_Training", "Model Training", "MT"),
        ("01_Machine_Learning/04_Evaluation", "Model Evaluation", "ME"),
        ("01_Machine_Learning/05_Applications", "ML Applications", "MLA"),
        ("01_Machine_Learning/06_Tools", "ML Tools", "MLT"),
        ("01_Machine_Learning/07_Projects", "ML Projects", "MLP"),
        
        # Deep Learning sub-folders
        ("02_Deep_Learning/01_Neural_Networks", "Neural Networks", "NN"),
        ("02_Deep_Learning/02_CNN", "Convolutional Neural Networks", "CNN"),
        ("02_Deep_Learning/03_RNN", "Recurrent Neural Networks", "RNN"),
        ("02_Deep_Learning/04_LSTM", "Long Short-Term Memory", "LSTM"),
        ("02_Deep_Learning/05_Transformers", "Transformer Networks", "TR"),
        ("02_Deep_Learning/06_Frameworks", "Deep Learning Frameworks", "DLF"),
        ("02_Deep_Learning/07_Applications", "Deep Learning Applications", "DLA"),
        
        # NLP sub-folders
        ("04_Natural_Language_Processing/01_Text_Processing", "Text Processing", "TP"),
        ("04_Natural_Language_Processing/02_Language_Models", "Language Models", "LM"),
        ("04_Natural_Language_Processing/03_Text_Classification", "Text Classification", "TC"),
        ("04_Natural_Language_Processing/04_Information_Extraction", "Information Extraction", "IE"),
        ("04_Natural_Language_Processing/05_Machine_Translation", "Machine Translation", "MT"),
        ("04_Natural_Language_Processing/06_Tools", "NLP Tools", "NLPT"),
        ("04_Natural_Language_Processing/07_Applications", "NLP Applications", "NLPA"),
        
        # Computer Vision sub-folders
        ("05_Computer_Vision/01_Image_Processing", "Image Processing", "IP"),
        ("05_Computer_Vision/02_Object_Detection", "Object Detection", "OD"),
        ("05_Computer_Vision/03_Image_Segmentation", "Image Segmentation", "IS"),
        ("05_Computer_Vision/04_Image_Generation", "Image Generation", "IG"),
        ("05_Computer_Vision/05_Video_Analysis", "Video Analysis", "VA"),
        ("05_Computer_Vision/06_Tools", "Computer Vision Tools", "CVT"),
        ("05_Computer_Vision/07_Applications", "Computer Vision Applications", "CVA")
    ]
    
    for folder_path, topic, category in sub_folders:
        create_generic_problems_file(folder_path, topic, category)
    
    print("\n🎉 Hoàn thành! Đã tạo 5 bài toán phức tạp cho:")
    print(f"   - {len(main_folders)} thư mục chính")
    print(f"   - {len(sub_folders)} thư mục con quan trọng")
    print(f"   - Tổng cộng: {len(main_folders) + len(sub_folders)} file COMPLEX_PROBLEMS.md")
    print("\n📝 Mỗi file chứa 5 bài toán phức tạp với:")
    print("   - Yêu cầu kỹ thuật nâng cao")
    print("   - Metrics đánh giá cụ thể")
    print("   - Công cụ và framework")
    print("   - Tài liệu tham khảo")

if __name__ == "__main__":
    main() 