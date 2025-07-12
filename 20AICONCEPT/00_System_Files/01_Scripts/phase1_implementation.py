#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 1 Implementation: Tạo nội dung cơ bản cho tất cả thư mục con, sửa lỗi nội suy chuỗi và đổi tên file theo topic.
"""

import os
from pathlib import Path

def sanitize_topic(topic):
    return topic.lower().replace(' ', '_').replace('-', '_')

def create_theory_file(folder_path, topic):
    """Tạo file THEORY_<topic>.md cho thư mục con"""
    topic_safe = sanitize_topic(topic)
    content = f'''# 📚 Lý Thuyết - {topic}

## 🎯 Tổng Quan

{topic} là một khái niệm quan trọng trong lĩnh vực AI/ML. Bài viết này sẽ cung cấp cái nhìn tổng quan về lý thuyết đằng sau {topic.lower()}.

## 📖 Khái Niệm Cơ Bản

### Định Nghĩa
{topic} là một phương pháp/kỹ thuật được sử dụng để...

### Nguyên Lý Hoạt Động
- **Principle 1**: Mô tả nguyên lý đầu tiên
- **Principle 2**: Mô tả nguyên lý thứ hai
- **Principle 3**: Mô tả nguyên lý thứ ba

### Ứng Dụng Thực Tế
- Ứng dụng trong lĩnh vực 1
- Ứng dụng trong lĩnh vực 2
- Ứng dụng trong lĩnh vực 3

## 🔬 Lý Thuyết Nâng Cao

### Mathematical Foundation
Các công thức toán học cơ bản:

    # Formula 1
    formula_1 = "y = f(x)"

    # Formula 2
    formula_2 = "loss = Σ(prediction - actual)²"

### Algorithmic Complexity
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Optimization**: Các phương pháp tối ưu

### Advantages & Disadvantages
**Ưu điểm:**
- Ưu điểm 1
- Ưu điểm 2
- Ưu điểm 3

**Nhược điểm:**
- Nhược điểm 1
- Nhược điểm 2
- Nhược điểm 3

## 📚 Tài Liệu Tham Khảo

1. **Book 1**: Author - Title (Year)
2. **Paper 1**: Author - Title (Year)
3. **Research 1**: Author - Title (Year)
4. **Online Course**: Course Name - Platform
5. **Documentation**: Official Documentation

## 🎯 Kết Luận

{topic} là một công cụ mạnh mẽ trong AI/ML, cung cấp nền tảng cho nhiều ứng dụng thực tế. Việc hiểu rõ lý thuyết đằng sau sẽ giúp bạn áp dụng hiệu quả trong các dự án thực tế.

## 🔗 Liên Kết Liên Quan

- [Implementation Guide](./IMPLEMENTATION_{topic_safe}.md)
- [Code Examples](./CODE_EXAMPLES_{topic_safe}.md)
- [Best Practices](./BEST_PRACTICES_{topic_safe}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
'''
    file_path = Path(folder_path) / f"THEORY_{topic_safe}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_implementation_file(folder_path, topic):
    """Tạo file IMPLEMENTATION_<topic>.md cho thư mục con"""
    topic_safe = sanitize_topic(topic)
    content = f'''# 🛠️ Implementation Guide - {topic}

## 🎯 Tổng Quan

Hướng dẫn chi tiết cách implement {topic.lower()} từ cơ bản đến nâng cao.

## 📋 Prerequisites

### Kiến Thức Cần Có
- Python programming (intermediate level)
- Basic mathematics (linear algebra, calculus)
- Data structures and algorithms
- Basic understanding of machine learning concepts

### Tools & Libraries

    # Core libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Machine Learning
    from sklearn import metrics, model_selection
    from sklearn.preprocessing import StandardScaler

    # Deep Learning (if applicable)
    import torch
    import tensorflow as tf

    # Visualization
    import plotly.express as px
    import plotly.graph_objects as go

## 🚀 Basic Implementation

### Step 1: Data Preparation

    # Load and prepare data
    def prepare_data(data_path):
        """
        Prepare data for {topic.lower()}
        Args:
            data_path: Path to data file
        Returns:
            X: Features
            y: Target variable
        """
        # Load data
        data = pd.read_csv(data_path)
        # Handle missing values
        data = data.dropna()
        # Separate features and target
        X = data.drop('target', axis=1)
        y = data['target']
        return X, y

### Step 2: Model Implementation

    # Basic implementation
    def basic_{topic_safe}(X, y):
        """
        Basic implementation of {topic.lower()}
        Args:
            X: Input features
            y: Target variable
        Returns:
            model: Trained model
        """
        # Implementation code here
        pass

### Step 3: Training and Evaluation

    # Train and evaluate model
    def train_and_evaluate(X, y):
        """
        Train and evaluate the model
        """
        # Split data
        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        # Train model
        model = basic_{topic_safe}(X_train, y_train)
        # Make predictions
        predictions = model.predict(X_test)
        # Evaluate
        accuracy = metrics.accuracy_score(y_test, predictions)
        return model, accuracy

## 🔧 Advanced Implementation

### Optimization Techniques
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Feature Engineering**: Feature selection, feature creation, dimensionality reduction
- **Ensemble Methods**: Combining multiple models
- **Cross-Validation**: K-fold, stratified, time series split

### Error Handling

    import logging
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    def robust_implementation(X, y):
        """
        Robust implementation with error handling
        """
        try:
            # Implementation with error handling
            model = basic_{topic_safe}(X, y)
            logger.info("Model trained successfully")
            return model
        except Exception as e:
            logger.error(f"Error training model: {{e}}")
            raise

### Performance Optimization

    # Performance optimization
    def optimized_implementation(X, y):
        """
        Optimized implementation for better performance
        """
        # Use vectorized operations
        # Minimize memory usage
        # Optimize for speed
        pass

## 📊 Evaluation

### Metrics
- **Accuracy**: Overall correctness
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area under the ROC curve

### Visualization

    def plot_results(y_true, y_pred):
        """
        Plot evaluation results
        """
        # Confusion matrix
        cm = metrics.confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()
        # ROC curve
        fpr, tpr, _ = metrics.roc_curve(y_true, y_pred)
        auc = metrics.auc(fpr, tpr)
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, label=f'ROC curve (AUC = {{auc:.2f}})')
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve')
        plt.legend()
        plt.show()

## 🎯 Best Practices

1. **Data Quality**: Always check data quality before implementation
2. **Feature Engineering**: Invest time in feature engineering
3. **Cross-Validation**: Use cross-validation to avoid overfitting
4. **Hyperparameter Tuning**: Tune hyperparameters systematically
5. **Documentation**: Document your implementation thoroughly

## 🚨 Common Mistakes

1. **Data Leakage**: Using test data during training
2. **Overfitting**: Model performs well on training but poorly on test
3. **Underfitting**: Model is too simple for the data
4. **Ignoring Data Distribution**: Not checking data distribution
5. **Not Scaling Features**: Using unscaled features when needed

## 📚 References

1. **Official Documentation**: Link to official docs
2. **Research Papers**: Relevant research papers
3. **Online Courses**: Recommended courses
4. **Books**: Recommended books
5. **Tutorials**: Online tutorials

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_{topic_safe}.md)
- [Code Examples](./CODE_EXAMPLES_{topic_safe}.md)
- [Best Practices](./BEST_PRACTICES_{topic_safe}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
'''
    file_path = Path(folder_path) / f"IMPLEMENTATION_{topic_safe}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_code_examples_file(folder_path, topic):
    """Tạo file CODE_EXAMPLES_<topic>.md cho thư mục con"""
    topic_safe = sanitize_topic(topic)
    content = f'''# 💻 Code Examples - {topic}

## 🎯 Tổng Quan

Các ví dụ code thực tế cho {topic.lower()}.

## 📚 Basic Examples

### Example 1: Simple Implementation

    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    def simple_{topic_safe}(X, y):
        """
        Simple implementation of {topic.lower()}
        Parameters:
        X: Input features (numpy array or pandas DataFrame)
        y: Target variable (numpy array or pandas Series)
        Returns:
        model: Trained model
        """
        # Implementation here
        pass

    # Usage example
    if __name__ == "__main__":
        # Load sample data
        from sklearn.datasets import make_classification
        X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train model
        model = simple_{topic_safe}(X_train, y_train)
        # Make predictions
        predictions = model.predict(X_test)
        # Evaluate
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {{accuracy:.4f}}")

## 🔧 Advanced Examples

### Example 2: Custom Implementation

    class Custom{topic.title().replace(' ', '').replace('-', '')}:
        """
        Custom implementation of {topic.lower()}
        """
        def __init__(self, learning_rate=0.01, max_iterations=1000):
            self.learning_rate = learning_rate
            self.max_iterations = max_iterations
            self.weights = None
            self.bias = None
            self.history = []
        def fit(self, X, y):
            n_samples, n_features = X.shape
            self.weights = np.zeros(n_features)
            self.bias = 0
            for iteration in range(self.max_iterations):
                predictions = self.predict(X)
                dw = (1/n_samples) * np.dot(X.T, (predictions - y))
                db = np.mean(predictions - y)
                self.weights -= self.learning_rate * dw
                self.bias -= self.learning_rate * db
                loss = np.mean((predictions - y) ** 2)
                self.history.append(loss)
                if len(self.history) > 10 and abs(self.history[-1] - self.history[-10]) < 1e-6:
                    break
        def predict(self, X):
            return np.dot(X, self.weights) + self.bias
        def plot_training_history(self):
            import matplotlib.pyplot as plt
            plt.figure(figsize=(10, 6))
            plt.plot(self.history)
            plt.title('Training History')
            plt.xlabel('Iteration')
            plt.ylabel('Loss')
            plt.grid(True)
            plt.show()

## 📚 References

1. **Official Documentation**: Link to official docs
2. **GitHub Examples**: Link to GitHub examples
3. **Online Tutorials**: Link to tutorials
4. **Research Papers**: Link to relevant papers
5. **Books**: Link to recommended books

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_{topic_safe}.md)
- [Implementation](./IMPLEMENTATION_{topic_safe}.md)
- [Best Practices](./BEST_PRACTICES_{topic_safe}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
'''
    file_path = Path(folder_path) / f"CODE_EXAMPLES_{topic_safe}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_best_practices_file(folder_path, topic):
    """Tạo file BEST_PRACTICES_<topic>.md cho thư mục con"""
    topic_safe = sanitize_topic(topic)
    content = f'''# ⭐ Best Practices - {topic}

## 🎯 Tổng Quan

Các best practices khi làm việc với {topic.lower()}.

- **Always validate data**
- **Use version control**
- **Document code and experiments**
- **Monitor model performance**
- **Follow security best practices**

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_{topic_safe}.md)
- [Implementation](./IMPLEMENTATION_{topic_safe}.md)
- [Code Examples](./CODE_EXAMPLES_{topic_safe}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
'''
    file_path = Path(folder_path) / f"BEST_PRACTICES_{topic_safe}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_requirements_file(folder_path, topic):
    topic_safe = sanitize_topic(topic)
    content = '''# Core Libraries
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0

# Machine Learning
scikit-learn>=1.0.0
xgboost>=1.5.0
lightgbm>=3.3.0

# Deep Learning (if needed)
tensorflow>=2.8.0
torch>=1.10.0
transformers>=4.20.0

# Data Processing
nltk>=3.7
opencv-python>=4.5.0
pillow>=8.3.0

# Visualization
plotly>=5.0.0
bokeh>=2.4.0

# Utilities
jupyter>=1.0.0
ipykernel>=6.0.0
'''
    file_path = Path(folder_path) / f"requirements_{topic_safe}.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def main():
    print("🚀 Phase 1: Bắt đầu tạo nội dung cơ bản cho tất cả thư mục con...")
    subdirs = []
    for root, dirs, files in os.walk('.'):
        if root == '.' or any(part.startswith('.') for part in Path(root).parts):
            continue
        subdirs.append((root, Path(root).name.replace('_', ' ').title()))
    created_count = 0
    for folder_path, topic in subdirs:
        try:
            existing_files = set()
            if Path(folder_path).exists():
                for file in Path(folder_path).glob("*.*"):
                    existing_files.add(file.name)
            topic_safe = sanitize_topic(topic)
            if f"THEORY_{topic_safe}.md" not in existing_files:
                create_theory_file(folder_path, topic)
            if f"IMPLEMENTATION_{topic_safe}.md" not in existing_files:
                create_implementation_file(folder_path, topic)
            if f"CODE_EXAMPLES_{topic_safe}.md" not in existing_files:
                create_code_examples_file(folder_path, topic)
            if f"BEST_PRACTICES_{topic_safe}.md" not in existing_files:
                create_best_practices_file(folder_path, topic)
            if f"requirements_{topic_safe}.txt" not in existing_files:
                create_requirements_file(folder_path, topic)
            created_count += 1
            print(f"✅ Enhanced: {folder_path}")
        except Exception as e:
            print(f"❌ Error creating content for {folder_path}: {e}")
    print(f"\n🎉 Phase 1 Hoàn thành! Đã tạo nội dung cơ bản cho {created_count} thư mục con")
    print("📝 Mỗi thư mục con giờ có:")
    print("   - THEORY_<topic>.md: Lý thuyết chi tiết")
    print("   - IMPLEMENTATION_<topic>.md: Hướng dẫn implement")
    print("   - CODE_EXAMPLES_<topic>.md: Ví dụ code")
    print("   - BEST_PRACTICES_<topic>.md: Best practices")
    print("   - requirements_<topic>.txt: Dependencies")
    print("   - COMPLEX_PROBLEMS.md: 5 bài toán phức tạp (đã có)")

if __name__ == "__main__":
    main() 