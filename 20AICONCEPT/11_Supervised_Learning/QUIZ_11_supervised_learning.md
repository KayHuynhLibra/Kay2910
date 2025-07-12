# 🧠 Quiz - 11 Supervised Learning

## 📝 Instructions / Hướng Dẫn

**Tiếng Việt:** Trả lời các câu hỏi sau để kiểm tra kiến thức về 11 Supervised Learning.

**English:** Answer the following questions to test your knowledge of 11 Supervised Learning.

## ❓ Questions / Câu Hỏi

### Question 1 / Câu Hỏi 1
**Tiếng Việt:** 11 Supervised Learning được sử dụng chủ yếu để làm gì?

**English:** What is 11 Supervised Learning primarily used for?

A) Data visualization / Minh họa dữ liệu  
B) Model training / Huấn luyện model  
C) Data preprocessing / Tiền xử lý dữ liệu  
D) All of the above / Tất cả các đáp án trên

### Question 2 / Câu Hỏi 2
**Tiếng Việt:** Trong 11 Supervised Learning, hyperparameter nào quan trọng nhất?

**English:** Which hyperparameter is most important in 11 Supervised Learning?

A) Learning rate / Tốc độ học  
B) Batch size / Kích thước batch  
C) Number of epochs / Số epoch  
D) Depends on the problem / Phụ thuộc vào bài toán

### Question 3 / Câu Hỏi 3
**Tiếng Việt:** Cách nào tốt nhất để đánh giá model 11 Supervised Learning?

**English:** What's the best way to evaluate a 11 Supervised Learning model?

A) Training accuracy / Độ chính xác training  
B) Test accuracy / Độ chính xác test  
C) Cross-validation / Cross-validation  
D) Validation accuracy / Độ chính xác validation

### Question 4 / Câu Hỏi 4
**Tiếng Việt:** Khi nào nên sử dụng 11 Supervised Learning?

**English:** When should you use 11 Supervised Learning?

A) Small datasets / Dữ liệu nhỏ  
B) Large datasets / Dữ liệu lớn  
C) Linear relationships / Mối quan hệ tuyến tính  
D) Non-linear relationships / Mối quan hệ phi tuyến

### Question 5 / Câu Hỏi 5
**Tiếng Việt:** Lỗi phổ biến nhất khi implement 11 Supervised Learning là gì?

**English:** What's the most common mistake when implementing 11 Supervised Learning?

A) Overfitting / Overfitting  
B) Underfitting / Underfitting  
C) Data leakage / Rò rỉ dữ liệu  
D) All of the above / Tất cả các đáp án trên

## 🔍 Code Challenge / Thử Thách Code

### Challenge 1 / Thử Thách 1
```python
# Implement a simple 11 Supervised Learning model
import numpy as np
from sklearn.model_selection import train_test_split

def implement_11_supervised_learning():
    '''
    Implement basic 11 Supervised Learning functionality
    '''
    # Generate sample data
    X = np.random.randn(100, 5)
    y = np.dot(X, np.random.randn(5)) + np.random.randn(100) * 0.1
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # TODO: Implement your 11 Supervised Learning model here
    # Hint: Use appropriate algorithm for 11 Supervised Learning
    
    # Return predictions
    return y_pred

# Test your implementation
predictions = implement_11_supervised_learning()
print(f"Predictions shape: {predictions.shape}")
```

### Challenge 2 / Thử Thách 2
```python
# Evaluate your 11 Supervised Learning model
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_11_supervised_learning_model(y_true, y_pred):
    '''
    Evaluate 11 Supervised Learning model performance
    '''
    # Calculate metrics
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # TODO: Add more evaluation metrics
    # Hint: Consider MAE, RMSE, etc.
    
    print(f"Model Evaluation Results:")
    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")
    
    return {'mse': mse, 'r2': r2}

# Test evaluation
# results = evaluate_11_supervised_learning_model(y_test, predictions)
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

- [Theory](./THEORY_11_supervised_learning.md)
- [Implementation](./IMPLEMENTATION_11_supervised_learning.md)
- [Code Examples](./CODE_EXAMPLES_11_supervised_learning.md)
- [Best Practices](./BEST_PRACTICES_11_supervised_learning.md)

## 🔗 Related Links / Liên Kết Liên Quan

- [Exercises](./EXERCISES_11_supervised_learning.md)
- [Project](./PROJECT_11_supervised_learning.md)
- [Learning Roadmap](./LEARNING_ROADMAP_11_supervised_learning.md)
