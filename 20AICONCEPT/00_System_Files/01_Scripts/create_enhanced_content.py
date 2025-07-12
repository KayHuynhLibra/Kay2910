#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo nội dung nâng cao cho tất cả thư mục AI/ML
"""

import os
from pathlib import Path

def create_theory_file(folder_path, topic):
    """Tạo file THEORY.md"""
    content = f"""# 📚 Lý Thuyết - {topic}

## 🎯 Tổng Quan

{topic} là một khái niệm cốt lõi trong lĩnh vực AI/ML. Bài viết này sẽ cung cấp cái nhìn tổng quan về lý thuyết đằng sau {topic.lower()}.

## 📖 Khái Niệm Cơ Bản

### Định Nghĩa
{topic} là...

### Nguyên Lý Hoạt Động
- **Principle 1**: Mô tả nguyên lý đầu tiên
- **Principle 2**: Mô tả nguyên lý thứ hai
- **Principle 3**: Mô tả nguyên lý thứ ba

### Ứng Dụng
- Ứng dụng 1
- Ứng dụng 2
- Ứng dụng 3

## 🔬 Lý Thuyết Nâng Cao

### Mathematical Foundation
Các công thức toán học cơ bản:

```python
# Formula 1
formula_1 = "y = ax + b"

# Formula 2
formula_2 = "loss = Σ(y_pred - y_true)²"
```

### Algorithmic Complexity
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Optimization**: Các phương pháp tối ưu

## 📚 Tài Liệu Tham Khảo

1. **Book 1**: Author - Title
2. **Paper 1**: Author - Title
3. **Research 1**: Author - Title

## 🎯 Kết Luận

{topic} là một công cụ mạnh mẽ trong AI/ML, cung cấp nền tảng cho nhiều ứng dụng thực tế.
"""
    
    file_path = Path(folder_path) / "THEORY.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_implementation_file(folder_path, topic):
    """Tạo file IMPLEMENTATION.md"""
    content = f"""# 🛠️ Implementation Guide - {topic}

## 🎯 Tổng Quan

Hướng dẫn chi tiết cách implement {topic.lower()} từ cơ bản đến nâng cao.

## 📋 Prerequisites

### Kiến Thức Cần Có
- Python programming
- Basic mathematics
- Data structures

### Tools & Libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
```

## 🚀 Basic Implementation

### Step 1: Data Preparation
```python
# Load data
data = pd.read_csv('data.csv')

# Preprocess data
X = data.drop('target', axis=1)
y = data['target']
```

### Step 2: Model Implementation
```python
# Basic implementation
def basic_{topic.lower().replace(' ', '_')}(X, y):
    # Implementation code here
    pass
```

### Step 3: Training
```python
# Train model
model = basic_{topic.lower().replace(' ', '_')}(X_train, y_train)
```

## 🔧 Advanced Implementation

### Optimization Techniques
- Technique 1
- Technique 2
- Technique 3

### Error Handling
```python
try:
    # Implementation with error handling
    pass
except Exception as e:
    print(f"Error: {{e}}")
```

## 📊 Evaluation

### Metrics
- Accuracy
- Precision
- Recall
- F1-Score

### Visualization
```python
# Plot results
plt.figure(figsize=(10, 6))
# Plotting code here
plt.show()
```

## 🎯 Best Practices

1. **Data Quality**: Ensure data quality
2. **Feature Engineering**: Proper feature engineering
3. **Validation**: Cross-validation
4. **Documentation**: Code documentation

## 🚨 Common Mistakes

1. **Mistake 1**: Description
2. **Mistake 2**: Description
3. **Mistake 3**: Description

## 📚 References

1. **Documentation**: Official docs
2. **Tutorials**: Online tutorials
3. **Examples**: Code examples
"""
    
    file_path = Path(folder_path) / "IMPLEMENTATION.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_code_examples_file(folder_path, topic):
    """Tạo file CODE_EXAMPLES.md"""
    content = f"""# 💻 Code Examples - {topic}

## 🎯 Tổng Quan

Các ví dụ code thực tế cho {topic.lower()}.

## 📚 Basic Examples

### Example 1: Simple Implementation
```python
import numpy as np
import pandas as pd

def simple_{topic.lower().replace(' ', '_')}(X, y):
    """
    Simple implementation of {topic.lower()}
    
    Parameters:
    X: Input features
    y: Target variable
    
    Returns:
    model: Trained model
    """
    # Implementation here
    return model

# Usage
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 0, 1])
model = simple_{topic.lower().replace(' ', '_')}(X, y)
```

### Example 2: With Scikit-learn
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('data.csv')
X = data.drop('target', axis=1)
y = data['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 🔧 Advanced Examples

### Example 3: Custom Implementation
```python
class Custom{topic.replace(' ', '')}:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        # Training implementation
        pass
    
    def predict(self, X):
        # Prediction implementation
        pass
```

### Example 4: With TensorFlow
```python
import tensorflow as tf

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(X.shape[1],))
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X_train, y_train, epochs=100, batch_size=32)
```

## 📊 Visualization Examples

### Example 5: Plotting Results
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Plot predictions vs actual
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Predictions vs Actual')
plt.show()
```

## 🎯 Performance Examples

### Example 6: Performance Metrics
```python
from sklearn.metrics import mean_squared_error, r2_score

# Calculate metrics
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'MSE: {{mse:.4f}}')
print(f'R²: {{r2:.4f}}')
```

## 🚀 Production Examples

### Example 7: API Implementation
```python
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
```

## 📚 References

1. **Official Documentation**: Link to official docs
2. **GitHub Examples**: Link to GitHub examples
3. **Online Tutorials**: Link to tutorials
"""
    
    file_path = Path(folder_path) / "CODE_EXAMPLES.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_best_practices_file(folder_path, topic):
    """Tạo file BEST_PRACTICES.md"""
    content = f"""# ⭐ Best Practices - {topic}

## 🎯 Tổng Quan

Các best practices khi làm việc với {topic.lower()}.

## 📋 Data Preparation

### ✅ Do's
- Clean and validate data thoroughly
- Handle missing values appropriately
- Scale features when necessary
- Split data properly (train/validation/test)

### ❌ Don'ts
- Don't ignore data quality issues
- Don't use test data for training
- Don't forget to normalize features
- Don't ignore outliers without analysis

## 🔧 Model Development

### ✅ Do's
- Start with simple models
- Use cross-validation
- Regularize when needed
- Document your approach

### ❌ Don'ts
- Don't overfit to training data
- Don't ignore model interpretability
- Don't skip validation steps
- Don't forget to save model artifacts

## 📊 Evaluation

### ✅ Do's
- Use multiple metrics
- Validate on unseen data
- Consider business context
- Monitor model drift

### ❌ Don'ts
- Don't rely on single metric
- Don't ignore domain knowledge
- Don't forget to test edge cases
- Don't skip error analysis

## 🚀 Production

### ✅ Do's
- Version control everything
- Implement proper logging
- Monitor performance
- Plan for scalability

### ❌ Don'ts
- Don't deploy without testing
- Don't ignore security concerns
- Don't forget backup strategies
- Don't skip documentation

## 📚 Code Quality

### ✅ Do's
- Write clean, readable code
- Add proper comments
- Use meaningful variable names
- Follow PEP 8 guidelines

### ❌ Don'ts
- Don't write spaghetti code
- Don't ignore error handling
- Don't use magic numbers
- Don't skip unit tests

## 🎯 Performance Optimization

### Memory Management
- Use generators for large datasets
- Clear variables when not needed
- Use appropriate data types

### Speed Optimization
- Vectorize operations when possible
- Use efficient algorithms
- Profile your code

## 🔒 Security

### Data Security
- Encrypt sensitive data
- Use secure connections
- Implement access controls

### Model Security
- Validate inputs
- Protect against adversarial attacks
- Monitor for anomalies

## 📈 Monitoring

### Model Performance
- Track key metrics
- Set up alerts
- Monitor data drift

### System Health
- Monitor resource usage
- Track error rates
- Check system logs

## 🎓 Learning Resources

1. **Books**: Recommended books
2. **Courses**: Online courses
3. **Papers**: Research papers
4. **Communities**: Online communities

## 📝 Checklist

### Before Implementation
- [ ] Understand requirements
- [ ] Plan approach
- [ ] Set up environment
- [ ] Prepare data

### During Implementation
- [ ] Follow coding standards
- [ ] Test regularly
- [ ] Document progress
- [ ] Validate results

### After Implementation
- [ ] Review code
- [ ] Test thoroughly
- [ ] Document everything
- [ ] Deploy carefully
"""
    
    file_path = Path(folder_path) / "BEST_PRACTICES.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_requirements_file(folder_path):
    """Tạo file requirements.txt"""
    content = """# Core Libraries
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0

# Machine Learning
scikit-learn>=1.0.0
xgboost>=1.5.0
lightgbm>=3.3.0

# Deep Learning
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
"""
    
    file_path = Path(folder_path) / "requirements.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def create_setup_file(folder_path, topic):
    """Tạo file SETUP.md"""
    content = f"""# 🚀 Setup Guide - {topic}

## 🎯 Tổng Quan

Hướng dẫn setup môi trường để làm việc với {topic.lower()}.

## 📋 Prerequisites

### System Requirements
- Python 3.8+
- 8GB RAM (minimum)
- 10GB free disk space

### Operating System
- Windows 10/11
- macOS 10.15+
- Ubuntu 18.04+

## 🐍 Python Setup

### Install Python
```bash
# Download from python.org
# Or use conda
conda create -n {topic.lower().replace(' ', '_')} python=3.9
conda activate {topic.lower().replace(' ', '_')}
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔧 IDE Setup

### VS Code
1. Install VS Code
2. Install Python extension
3. Install Jupyter extension
4. Configure Python interpreter

### PyCharm
1. Install PyCharm
2. Create new project
3. Configure virtual environment
4. Install required packages

## 📊 Data Setup

### Download Datasets
```python
# Example dataset download
import pandas as pd
from sklearn.datasets import load_boston

# Load sample data
data = load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.to_csv('sample_data.csv', index=False)
```

### Data Structure
```
data/
├── raw/           # Raw data files
├── processed/     # Processed data files
├── external/      # External data sources
└── interim/       # Intermediate data files
```

## 🧪 Testing Setup

### Install Testing Libraries
```bash
pip install pytest
pip install pytest-cov
pip install pytest-mock
```

### Run Tests
```bash
pytest tests/
pytest --cov=src tests/
```

## 📚 Jupyter Setup

### Install Jupyter
```bash
pip install jupyter
pip install ipykernel
```

### Start Jupyter
```bash
jupyter notebook
# or
jupyter lab
```

## 🔍 Debugging Setup

### VS Code Debugging
1. Create launch.json
2. Set breakpoints
3. Start debugging session

### PyCharm Debugging
1. Configure run configuration
2. Set breakpoints
3. Start debug session

## 📈 Monitoring Setup

### Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Performance Monitoring
```python
import time
import psutil

def monitor_performance():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    return cpu_percent, memory_percent
```

## 🚀 Deployment Setup

### Docker Setup
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]
```

### Cloud Deployment
- AWS SageMaker
- Google Cloud AI Platform
- Azure Machine Learning

## 📝 Verification

### Test Installation
```python
# Test imports
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import torch

print("All packages installed successfully!")
```

### Test Data Loading
```python
# Test data loading
import pandas as pd
data = pd.read_csv('sample_data.csv')
print(f"Data shape: {{data.shape}}")
```

## 🆘 Troubleshooting

### Common Issues
1. **Import Error**: Check Python path
2. **Memory Error**: Reduce batch size
3. **Version Conflict**: Use virtual environment

### Getting Help
- Check documentation
- Search Stack Overflow
- Ask in community forums

## 📚 Next Steps

1. Read THEORY.md
2. Follow IMPLEMENTATION.md
3. Practice with CODE_EXAMPLES.md
4. Apply BEST_PRACTICES.md
"""
    
    file_path = Path(folder_path) / "SETUP.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")

def main():
    """Main function để tạo nội dung nâng cao"""
    
    print("🚀 Bắt đầu tạo nội dung nâng cao cho tất cả thư mục...")
    
    # Lấy tất cả thư mục con
    subdirs = []
    for root, dirs, files in os.walk('.'):
        if root == '.' or any(part.startswith('.') for part in Path(root).parts):
            continue
            
        if len(Path(root).parts) > 1:
            for dir_name in dirs:
                full_path = Path(root) / dir_name
                topic = dir_name.replace('_', ' ').title()
                subdirs.append((str(full_path), topic))
    
    # Tạo nội dung nâng cao cho các thư mục
    created_count = 0
    for folder_path, topic in subdirs:
        try:
            # Tạo các file cơ bản
            create_theory_file(folder_path, topic)
            create_implementation_file(folder_path, topic)
            create_code_examples_file(folder_path, topic)
            create_best_practices_file(folder_path, topic)
            create_requirements_file(folder_path)
            create_setup_file(folder_path, topic)
            
            created_count += 1
            print(f"✅ Enhanced: {folder_path}")
            
        except Exception as e:
            print(f"❌ Error creating content for {folder_path}: {e}")
    
    print(f"\n🎉 Hoàn thành! Đã tạo nội dung nâng cao cho {created_count} thư mục")
    print("📝 Mỗi thư mục giờ có:")
    print("   - THEORY.md: Lý thuyết chi tiết")
    print("   - IMPLEMENTATION.md: Hướng dẫn implement")
    print("   - CODE_EXAMPLES.md: Ví dụ code")
    print("   - BEST_PRACTICES.md: Best practices")
    print("   - requirements.txt: Dependencies")
    print("   - SETUP.md: Hướng dẫn setup")

if __name__ == "__main__":
    main() 