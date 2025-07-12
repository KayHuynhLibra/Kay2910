# 🧠 Quiz - 02 Spam Detection

## 📝 Instructions / Hướng Dẫn

**Tiếng Việt:** Trả lời các câu hỏi sau để kiểm tra kiến thức về 02 Spam Detection.

**English:** Answer the following questions to test your knowledge of 02 Spam Detection.

## ❓ Questions / Câu Hỏi

### Question 1 / Câu Hỏi 1
**Tiếng Việt:** 02 Spam Detection được sử dụng chủ yếu để làm gì?

**English:** What is 02 Spam Detection primarily used for?

A) Data visualization / Minh họa dữ liệu  
B) Model training / Huấn luyện model  
C) Data preprocessing / Tiền xử lý dữ liệu  
D) All of the above / Tất cả các đáp án trên

### Question 2 / Câu Hỏi 2
**Tiếng Việt:** Trong 02 Spam Detection, hyperparameter nào quan trọng nhất?

**English:** Which hyperparameter is most important in 02 Spam Detection?

A) Learning rate / Tốc độ học  
B) Batch size / Kích thước batch  
C) Number of epochs / Số epoch  
D) Depends on the problem / Phụ thuộc vào bài toán

### Question 3 / Câu Hỏi 3
**Tiếng Việt:** Cách nào tốt nhất để đánh giá model 02 Spam Detection?

**English:** What's the best way to evaluate a 02 Spam Detection model?

A) Training accuracy / Độ chính xác training  
B) Test accuracy / Độ chính xác test  
C) Cross-validation / Cross-validation  
D) Validation accuracy / Độ chính xác validation

### Question 4 / Câu Hỏi 4
**Tiếng Việt:** Khi nào nên sử dụng 02 Spam Detection?

**English:** When should you use 02 Spam Detection?

A) Small datasets / Dữ liệu nhỏ  
B) Large datasets / Dữ liệu lớn  
C) Linear relationships / Mối quan hệ tuyến tính  
D) Non-linear relationships / Mối quan hệ phi tuyến

### Question 5 / Câu Hỏi 5
**Tiếng Việt:** Lỗi phổ biến nhất khi implement 02 Spam Detection là gì?

**English:** What's the most common mistake when implementing 02 Spam Detection?

A) Overfitting / Overfitting  
B) Underfitting / Underfitting  
C) Data leakage / Rò rỉ dữ liệu  
D) All of the above / Tất cả các đáp án trên

## 🔍 Code Challenge / Thử Thách Code

### Challenge 1 / Thử Thách 1
```python
# Implement a simple 02 Spam Detection model
import numpy as np
from sklearn.model_selection import train_test_split

def implement_02_spam_detection():
    '''
    Implement basic 02 Spam Detection functionality
    '''
    # Generate sample data
    X = np.random.randn(100, 5)
    y = np.dot(X, np.random.randn(5)) + np.random.randn(100) * 0.1
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # TODO: Implement your 02 Spam Detection model here
    # Hint: Use appropriate algorithm for 02 Spam Detection
    
    # Return predictions
    return y_pred

# Test your implementation
predictions = implement_02_spam_detection()
print(f"Predictions shape: {predictions.shape}")
```

### Challenge 2 / Thử Thách 2
```python
# Evaluate your 02 Spam Detection model
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_02_spam_detection_model(y_true, y_pred):
    '''
    Evaluate 02 Spam Detection model performance
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
# results = evaluate_02_spam_detection_model(y_test, predictions)
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

- [Theory](./THEORY_02_spam_detection.md)
- [Implementation](./IMPLEMENTATION_02_spam_detection.md)
- [Code Examples](./CODE_EXAMPLES_02_spam_detection.md)
- [Best Practices](./BEST_PRACTICES_02_spam_detection.md)

## 🔗 Related Links / Liên Kết Liên Quan

- [Exercises](./EXERCISES_02_spam_detection.md)
- [Project](./PROJECT_02_spam_detection.md)
- [Learning Roadmap](./LEARNING_ROADMAP_02_spam_detection.md)
