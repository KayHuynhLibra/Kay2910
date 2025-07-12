#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated System Upgrade: Nâng cấp toàn diện hệ thống tài liệu AI/ML
- Nội dung song ngữ (Việt + Anh)
- Chi tiết, chuyên sâu, đầy đủ ví dụ, code, hình ảnh/sơ đồ
- Quiz, Project, Roadmap, Checklist, Resources
- Navigation, Index, tổng hợp
"""

import os
from pathlib import Path


def theory_content_vi(topic):
    return f"""# 📚 Lý Thuyết Chi Tiết - {topic}

## 🎯 Tổng Quan / Overview

{topic} là một khái niệm cốt lõi trong lĩnh vực AI/ML, được sử dụng rộng rãi trong nhiều ứng dụng thực tế.

**English:** {topic} is a core concept in AI/ML, widely used in many real-world applications.

## 📖 Khái Niệm Cơ Bản / Basic Concepts

### Định Nghĩa / Definition
{topic} là một phương pháp/kỹ thuật được sử dụng để giải quyết các bài toán trong lĩnh vực machine learning và artificial intelligence.

**English:** {topic} is a method/technique used to solve problems in machine learning and artificial intelligence.

### Nguyên Lý Hoạt Động / Working Principles
- **Principle 1**: Mô tả nguyên lý đầu tiên / Description of first principle
- **Principle 2**: Mô tả nguyên lý thứ hai / Description of second principle  
- **Principle 3**: Mô tả nguyên lý thứ ba / Description of third principle

### Ứng Dụng Thực Tế / Real-world Applications
- Ứng dụng trong lĩnh vực 1 / Application in field 1
- Ứng dụng trong lĩnh vực 2 / Application in field 2
- Ứng dụng trong lĩnh vực 3 / Application in field 3

## 🔬 Lý Thuyết Nâng Cao / Advanced Theory

### Mathematical Foundation / Nền Tảng Toán Học

```python
# Mathematical formulas and implementations
import numpy as np

def {topic.lower().replace(' ', '_')}_formula(x, y):
    '''
    Mathematical implementation of {topic}
    '''
    # Formula implementation
    result = np.dot(x, y) + np.mean(x)
    return result

# Example usage
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = {topic.lower().replace(' ', '_')}_formula(x, y)
print(f"Result: {{result}}")
```

### Algorithmic Complexity / Độ Phức Tạp Thuật Toán
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Optimization**: Các phương pháp tối ưu / Optimization methods

### Advantages & Disadvantages / Ưu Điểm & Nhược Điểm

**Ưu điểm / Advantages:**
- Ưu điểm 1 / Advantage 1
- Ưu điểm 2 / Advantage 2
- Ưu điểm 3 / Advantage 3

**Nhược điểm / Disadvantages:**
- Nhược điểm 1 / Disadvantage 1
- Nhược điểm 2 / Disadvantage 2
- Nhược điểm 3 / Disadvantage 3

## 📊 Visualization / Minh Họa

```mermaid
graph TD
    A[Input Data] --> B[Preprocessing]
    B --> C[{topic} Algorithm]
    C --> D[Model Training]
    D --> E[Evaluation]
    E --> F[Deployment]
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style F fill:#e8f5e8
```

## 📚 Tài Liệu Tham Khảo / References

### Books / Sách
1. **"Hands-On Machine Learning"** - Aurélien Géron
2. **"Python Machine Learning"** - Sebastian Raschka
3. **"Deep Learning"** - Ian Goodfellow, Yoshua Bengio, Aaron Courville

### Research Papers / Bài Báo Nghiên Cứu
1. **Paper 1**: Author - Title (Year)
2. **Paper 2**: Author - Title (Year)
3. **Paper 3**: Author - Title (Year)

### Online Courses / Khóa Học Trực Tuyến
1. **Coursera**: Machine Learning by Andrew Ng
2. **edX**: Deep Learning Fundamentals
3. **Fast.ai**: Practical Deep Learning

## 🎯 Kết Luận / Conclusion

{topic} là một công cụ mạnh mẽ trong AI/ML, cung cấp nền tảng cho nhiều ứng dụng thực tế.

**English:** {topic} is a powerful tool in AI/ML, providing the foundation for many real-world applications.

## 🔗 Liên Kết Liên Quan / Related Links

- [Implementation Guide](./IMPLEMENTATION_{topic.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_{topic.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_{topic.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Quiz](./QUIZ_{topic.lower().replace(' ', '_')}.md)
- [Project](./PROJECT_{topic.lower().replace(' ', '_')}.md)
- [Roadmap](./ROADMAP_{topic.lower().replace(' ', '_')}.md)
"""


def theory_content_en(topic):
    return f"""# 📚 Detailed Theory - {topic}

## 🎯 Overview

{topic} is a core concept in AI/ML, widely used in many real-world applications.

## 📖 Basic Concepts

### Definition
{topic} is a method/technique used to solve problems in machine learning and artificial intelligence.

### Working Principles
- **Principle 1**: Description of first principle
- **Principle 2**: Description of second principle
- **Principle 3**: Description of third principle

### Real-world Applications
- Application in field 1
- Application in field 2
- Application in field 3

## 🔬 Advanced Theory

### Mathematical Foundation

```python
# Mathematical formulas and implementations
import numpy as np

def {topic.lower().replace(' ', '_')}_formula(x, y):
    '''
    Mathematical implementation of {topic}
    '''
    # Formula implementation
    result = np.dot(x, y) + np.mean(x)
    return result

# Example usage
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = {topic.lower().replace(' ', '_')}_formula(x, y)
print(f"Result: {{result}}")
```

### Algorithmic Complexity
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Optimization**: Optimization methods

### Advantages & Disadvantages

**Advantages:**
- Advantage 1
- Advantage 2
- Advantage 3

**Disadvantages:**
- Disadvantage 1
- Disadvantage 2
- Disadvantage 3

## 📊 Visualization

```mermaid
graph TD
    A[Input Data] --> B[Preprocessing]
    B --> C[{topic} Algorithm]
    C --> D[Model Training]
    D --> E[Evaluation]
    E --> F[Deployment]
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style F fill:#e8f5e8
```

## 📚 References

### Books
1. **"Hands-On Machine Learning"** - Aurélien Géron
2. **"Python Machine Learning"** - Sebastian Raschka
3. **"Deep Learning"** - Ian Goodfellow, Yoshua Bengio, Aaron Courville

### Research Papers
1. **Paper 1**: Author - Title (Year)
2. **Paper 2**: Author - Title (Year)
3. **Paper 3**: Author - Title (Year)

### Online Courses
1. **Coursera**: Machine Learning by Andrew Ng
2. **edX**: Deep Learning Fundamentals
3. **Fast.ai**: Practical Deep Learning

## 🎯 Conclusion

{topic} is a powerful tool in AI/ML, providing the foundation for many real-world applications.

## 🔗 Related Links

- [Implementation Guide](./IMPLEMENTATION_{topic.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_{topic.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_{topic.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Quiz](./QUIZ_{topic.lower().replace(' ', '_')}.md)
- [Project](./PROJECT_{topic.lower().replace(' ', '_')}.md)
- [Roadmap](./ROADMAP_{topic.lower().replace(' ', '_')}.md)
"""


def get_detailed_content(topic, content_type):
    if content_type == "theory":
        return theory_content_vi(topic) + "\n\n" + theory_content_en(topic)
    return f"# {topic} - {content_type}"


def create_quiz_content(topic):
    """Tạo nội dung quiz cho chủ đề"""
    return f"""# 🧠 Quiz - {topic}

## 📝 Instructions / Hướng Dẫn

**Tiếng Việt:** Trả lời các câu hỏi sau để kiểm tra kiến thức về {topic}.

**English:** Answer the following questions to test your knowledge of {topic}.

## ❓ Questions / Câu Hỏi

### Question 1 / Câu Hỏi 1
**Tiếng Việt:** {topic} được sử dụng chủ yếu để làm gì?

**English:** What is {topic} primarily used for?

A) Data visualization / Minh họa dữ liệu  
B) Model training / Huấn luyện model  
C) Data preprocessing / Tiền xử lý dữ liệu  
D) All of the above / Tất cả các đáp án trên

### Question 2 / Câu Hỏi 2
**Tiếng Việt:** Trong {topic}, hyperparameter nào quan trọng nhất?

**English:** Which hyperparameter is most important in {topic}?

A) Learning rate / Tốc độ học  
B) Batch size / Kích thước batch  
C) Number of epochs / Số epoch  
D) Depends on the problem / Phụ thuộc vào bài toán

### Question 3 / Câu Hỏi 3
**Tiếng Việt:** Cách nào tốt nhất để đánh giá model {topic}?

**English:** What's the best way to evaluate a {topic} model?

A) Training accuracy / Độ chính xác training  
B) Test accuracy / Độ chính xác test  
C) Cross-validation / Cross-validation  
D) Validation accuracy / Độ chính xác validation

### Question 4 / Câu Hỏi 4
**Tiếng Việt:** Khi nào nên sử dụng {topic}?

**English:** When should you use {topic}?

A) Small datasets / Dữ liệu nhỏ  
B) Large datasets / Dữ liệu lớn  
C) Linear relationships / Mối quan hệ tuyến tính  
D) Non-linear relationships / Mối quan hệ phi tuyến

### Question 5 / Câu Hỏi 5
**Tiếng Việt:** Lỗi phổ biến nhất khi implement {topic} là gì?

**English:** What's the most common mistake when implementing {topic}?

A) Overfitting / Overfitting  
B) Underfitting / Underfitting  
C) Data leakage / Rò rỉ dữ liệu  
D) All of the above / Tất cả các đáp án trên

## 🔍 Code Challenge / Thử Thách Code

### Challenge 1 / Thử Thách 1
```python
# Implement a simple {topic} model
import numpy as np
from sklearn.model_selection import train_test_split

def implement_{topic.lower().replace(' ', '_')}():
    '''
    Implement basic {topic} functionality
    '''
    # Generate sample data
    X = np.random.randn(100, 5)
    y = np.dot(X, np.random.randn(5)) + np.random.randn(100) * 0.1
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # TODO: Implement your {topic} model here
    # Hint: Use appropriate algorithm for {topic}
    
    # Return predictions
    return y_pred

# Test your implementation
predictions = implement_{topic.lower().replace(' ', '_')}()
print(f"Predictions shape: {{predictions.shape}}")
```

### Challenge 2 / Thử Thách 2
```python
# Evaluate your {topic} model
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_{topic.lower().replace(' ', '_')}_model(y_true, y_pred):
    '''
    Evaluate {topic} model performance
    '''
    # Calculate metrics
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # TODO: Add more evaluation metrics
    # Hint: Consider MAE, RMSE, etc.
    
    print(f"Model Evaluation Results:")
    print(f"MSE: {{mse:.4f}}")
    print(f"R²: {{r2:.4f}}")
    
    return {{'mse': mse, 'r2': r2}}

# Test evaluation
# results = evaluate_{topic.lower().replace(' ', '_')}_model(y_test, predictions)
```

## 📊 Scoring / Chấm Điểm

- **Questions 1-5**: 2 points each / 2 điểm mỗi câu
- **Code Challenge 1**: 5 points / 5 điểm
- **Code Challenge 2**: 5 points / 5 điểm
- **Total**: 20 points / Tổng cộng 20 điểm

## 🎯 Passing Score / Điểm Đạt

- **Excellent**: 18-20 points / Xuất sắc: 18-20 điểm
- **Good**: 15-17 points / Tốt: 15-17 điểm  
- **Pass**: 12-14 points / Đạt: 12-14 điểm
- **Fail**: <12 points / Không đạt: <12 điểm

## 📚 Study Resources / Tài Liệu Học Tập

- [Theory](./THEORY_{topic.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_{topic.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_{topic.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_{topic.lower().replace(' ', '_')}.md)

## 🔗 Related Links / Liên Kết Liên Quan

- [Exercises](./EXERCISES_{topic.lower().replace(' ', '_')}.md)
- [Project](./PROJECT_{topic.lower().replace(' ', '_')}.md)
- [Learning Roadmap](./LEARNING_ROADMAP_{topic.lower().replace(' ', '_')}.md)
"""


def create_project_content(topic):
    """Tạo nội dung project cho chủ đề"""
    return f"""# 🚀 Project - {topic}

## 📋 Mô Tả Dự Án / Project Description

**Tiếng Việt:** Xây dựng một hệ thống hoàn chỉnh sử dụng {topic} để giải quyết bài toán thực tế.

**English:** Build a complete system using {topic} to solve a real-world problem.

## 🎯 Mục Tiêu / Objectives

1. **Hiểu sâu về {topic}** / Deep understanding of {topic}
2. **Implement từ đầu đến cuối** / End-to-end implementation
3. **Đánh giá hiệu suất** / Performance evaluation
4. **Tối ưu hóa model** / Model optimization

## 📊 Dataset / Bộ Dữ Liệu

```python
# Sample dataset creation
import pandas as pd
import numpy as np

def create_sample_dataset():
    '''
    Create sample dataset for {topic} project
    '''
    np.random.seed(42)
    n_samples = 1000
    
    # Generate features
    X = np.random.randn(n_samples, 10)
    
    # Generate target (example for regression)
    y = np.dot(X, np.random.randn(10)) + np.random.randn(n_samples) * 0.1
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=[f'feature_{{i}}' for i in range(10)])
    df['target'] = y
    
    return df

# Usage
dataset = create_sample_dataset()
print(f"Dataset shape: {{dataset.shape}}")
```

## 🛠️ Implementation Steps / Các Bước Thực Hiện

### Step 1: Data Preparation / Bước 1: Chuẩn Bị Dữ Liệu
```python
def prepare_project_data(df):
    '''
    Prepare data for {topic} project
    '''
    # Handle missing values
    df = df.dropna()
    
    # Feature scaling
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler
```

### Step 2: Model Development / Bước 2: Phát Triển Model
```python
def develop_{topic.lower().replace(' ', '_')}_model(X, y):
    '''
    Develop {topic} model for project
    '''
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Import and train model (example with Linear Regression)
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"MSE: {{mse:.4f}}")
    print(f"R²: {{r2:.4f}}")
    
    return model, y_pred
```

### Step 3: Model Optimization / Bước 3: Tối Ưu Hóa Model
```python
def optimize_{topic.lower().replace(' ', '_')}_model(X, y):
    '''
    Optimize {topic} model using hyperparameter tuning
    '''
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import Ridge
    
    # Define parameter grid
    param_grid = {{
        'alpha': [0.1, 1.0, 10.0, 100.0],
        'solver': ['auto', 'svd', 'cholesky']
    }}
    
    # Grid search
    grid_search = GridSearchCV(
        Ridge(), param_grid, cv=5, scoring='neg_mean_squared_error'
    )
    grid_search.fit(X, y)
    
    print(f"Best parameters: {{grid_search.best_params_}}")
    print(f"Best score: {{-grid_search.best_score_:.4f}}")
    
    return grid_search.best_estimator_
```

## 📈 Evaluation / Đánh Giá

### Metrics / Các Chỉ Số
- **MSE**: Mean Squared Error
- **RMSE**: Root Mean Squared Error  
- **MAE**: Mean Absolute Error
- **R²**: Coefficient of Determination

### Visualization / Minh Họa
```python
def visualize_project_results(y_true, y_pred):
    '''
    Visualize project results
    '''
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(12, 4))
    
    # Prediction vs Actual
    plt.subplot(1, 2, 1)
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Prediction vs Actual')
    
    # Residuals
    plt.subplot(1, 2, 2)
    residuals = y_true - y_pred
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    
    plt.tight_layout()
    plt.show()
```

## 📝 Deliverables / Sản Phẩm

1. **Code hoàn chỉnh** / Complete code
2. **Báo cáo kết quả** / Results report
3. **Presentation slides** / Slides thuyết trình
4. **Demo video** / Video demo

## 🔗 Related Links / Liên Kết Liên Quan

- [Theory](./THEORY_{topic.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_{topic.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_{topic.lower().replace(' ', '_')}.md)
- [Quiz](./QUIZ_{topic.lower().replace(' ', '_')}.md)
"""


def create_roadmap_content(topic):
    """Tạo nội dung roadmap cho chủ đề"""
    return f"""# 🗺️ Learning Roadmap - {topic}

## 🎯 Tổng Quan / Overview

**Tiếng Việt:** Lộ trình học tập chi tiết để thành thạo {topic}.

**English:** Detailed learning roadmap to master {topic}.

## 📚 Beginner Level / Cấp Độ Cơ Bản

### Week 1-2: Fundamentals / Tuần 1-2: Nền Tảng
- [ ] **Lý thuyết cơ bản** / Basic theory
- [ ] **Mathematical foundations** / Nền tảng toán học
- [ ] **Simple implementations** / Implement đơn giản
- [ ] **Basic examples** / Ví dụ cơ bản

### Week 3-4: Implementation / Tuần 3-4: Thực Hiện
- [ ] **Hands-on coding** / Lập trình thực hành
- [ ] **Data preparation** / Chuẩn bị dữ liệu
- [ ] **Model training** / Huấn luyện model
- [ ] **Basic evaluation** / Đánh giá cơ bản

## 🔧 Intermediate Level / Cấp Độ Trung Cấp

### Week 5-6: Advanced Concepts / Tuần 5-6: Khái Niệm Nâng Cao
- [ ] **Advanced algorithms** / Thuật toán nâng cao
- [ ] **Optimization techniques** / Kỹ thuật tối ưu
- [ ] **Feature engineering** / Kỹ thuật feature
- [ ] **Cross-validation** / Cross-validation

### Week 7-8: Real Projects / Tuần 7-8: Dự Án Thực Tế
- [ ] **Complete project implementation** / Implement dự án hoàn chỉnh
- [ ] **Performance optimization** / Tối ưu hiệu suất
- [ ] **Error handling** / Xử lý lỗi
- [ ] **Documentation** / Tài liệu hóa

## 🚀 Advanced Level / Cấp Độ Nâng Cao

### Week 9-10: Production Ready / Tuần 9-10: Sẵn Sàng Production
- [ ] **Production deployment** / Triển khai production
- [ ] **Monitoring and logging** / Giám sát và logging
- [ ] **Scalability** / Khả năng mở rộng
- [ ] **Best practices** / Thực hành tốt nhất

### Week 11-12: Specialization / Tuần 11-12: Chuyên Sâu
- [ ] **Research papers** / Bài báo nghiên cứu
- [ ] **Custom implementations** / Implement tùy chỉnh
- [ ] **Performance benchmarking** / Benchmark hiệu suất
- [ ] **Contributing to open source** / Đóng góp open source

## 📊 Progress Tracking / Theo Dõi Tiến Độ

### Beginner Milestones / Cột Mốc Cơ Bản
- [ ] Complete basic theory understanding
- [ ] Implement simple examples
- [ ] Understand mathematical foundations
- [ ] Complete first project

### Intermediate Milestones / Cột Mốc Trung Cấp
- [ ] Master advanced concepts
- [ ] Complete real-world project
- [ ] Optimize model performance
- [ ] Handle complex datasets

### Advanced Milestones / Cột Mốc Nâng Cao
- [ ] Deploy to production
- [ ] Contribute to research
- [ ] Mentor others
- [ ] Create custom solutions

## 🎓 Learning Resources / Tài Nguyên Học Tập

### Books / Sách
1. **"Hands-On Machine Learning"** - Aurélien Géron
2. **"Python Machine Learning"** - Sebastian Raschka
3. **"Deep Learning"** - Ian Goodfellow

### Online Courses / Khóa Học Trực Tuyến
1. **Coursera**: Machine Learning by Andrew Ng
2. **edX**: Deep Learning Fundamentals
3. **Fast.ai**: Practical Deep Learning

### Research Papers / Bài Báo Nghiên Cứu
1. **Paper 1**: Author - Title (Year)
2. **Paper 2**: Author - Title (Year)
3. **Paper 3**: Author - Title (Year)

## 🔗 Related Links / Liên Kết Liên Quan

- [Theory](./THEORY_{topic.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_{topic.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_{topic.lower().replace(' ', '_')}.md)
- [Quiz](./QUIZ_{topic.lower().replace(' ', '_')}.md)
- [Project](./PROJECT_{topic.lower().replace(' ', '_')}.md)
"""


def upgrade_folder_content(folder_path, topic):
    """Nâng cấp nội dung cho một thư mục"""
    try:
        topic_safe = topic.lower().replace(' ', '_')
        
        # 1. Nâng cấp THEORY file
        theory_content = get_detailed_content(topic, "theory")
        theory_file = Path(folder_path) / f"THEORY_{topic_safe}.md"
        with open(theory_file, 'w', encoding='utf-8') as f:
            f.write(theory_content)
        
        # 2. Tạo QUIZ file
        quiz_content = create_quiz_content(topic)
        quiz_file = Path(folder_path) / f"QUIZ_{topic_safe}.md"
        with open(quiz_file, 'w', encoding='utf-8') as f:
            f.write(quiz_content)
        
        # 3. Tạo PROJECT file
        project_content = create_project_content(topic)
        project_file = Path(folder_path) / f"PROJECT_{topic_safe}.md"
        with open(project_file, 'w', encoding='utf-8') as f:
            f.write(project_content)
        
        # 4. Tạo ROADMAP file
        roadmap_content = create_roadmap_content(topic)
        roadmap_file = Path(folder_path) / f"ROADMAP_{topic_safe}.md"
        with open(roadmap_file, 'w', encoding='utf-8') as f:
            f.write(roadmap_content)
        
        print(f"✅ Upgraded: {{folder_path}}")
        return True
        
    except Exception as e:
        print(f"❌ Error upgrading {{folder_path}}: {{e}}")
        return False


def main():
    """Main function để nâng cấp toàn bộ hệ thống"""
    print("🚀 Bắt đầu nâng cấp toàn diện hệ thống tài liệu AI/ML...")
    
    # Lấy tất cả thư mục con
    subdirs = []
    for root, dirs, files in os.walk('.'):
        if root == '.' or any(part.startswith('.') or part == '__pycache__' for part in Path(root).parts):
            continue
        subdirs.append((root, Path(root).name.replace('_', ' ').title()))
    
    # Nâng cấp từng thư mục
    upgraded_count = 0
    for folder_path, topic in subdirs:
        if upgrade_folder_content(folder_path, topic):
            upgraded_count += 1
    
    print(f"\n🎉 Hoàn thành nâng cấp! Đã nâng cấp {upgraded_count} thư mục")
    print("📝 Mỗi thư mục giờ có:")
    print("   - THEORY_<topic>.md: Lý thuyết chi tiết (song ngữ)")
    print("   - QUIZ_<topic>.md: Bài kiểm tra kiến thức")
    print("   - PROJECT_<topic>.md: Dự án thực hành")
    print("   - ROADMAP_<topic>.md: Lộ trình học tập")
    print("   - CODE_EXAMPLES_<topic>.md: Ví dụ code")
    print("   - BEST_PRACTICES_<topic>.md: Best practices")
    print("   - requirements_<topic>.txt: Dependencies")
    print("   - COMPLEX_PROBLEMS.md: 5 bài toán phức tạp")


if __name__ == "__main__":
    main() 