# 🚀 Project - 04 Cross Modal Embeddings

## 📋 Mô Tả Dự Án / Project Description

**Tiếng Việt:** Xây dựng một hệ thống hoàn chỉnh sử dụng 04 Cross Modal Embeddings để giải quyết bài toán thực tế.

**English:** Build a complete system using 04 Cross Modal Embeddings to solve a real-world problem.

## 🎯 Mục Tiêu / Objectives

1. **Hiểu sâu về 04 Cross Modal Embeddings** / Deep understanding of 04 Cross Modal Embeddings
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
    Create sample dataset for 04 Cross Modal Embeddings project
    '''
    np.random.seed(42)
    n_samples = 1000
    
    # Generate features
    X = np.random.randn(n_samples, 10)
    
    # Generate target (example for regression)
    y = np.dot(X, np.random.randn(10)) + np.random.randn(n_samples) * 0.1
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
    df['target'] = y
    
    return df

# Usage
dataset = create_sample_dataset()
print(f"Dataset shape: {dataset.shape}")
```

## 🛠️ Implementation Steps / Các Bước Thực Hiện

### Step 1: Data Preparation / Bước 1: Chuẩn Bị Dữ Liệu
```python
def prepare_project_data(df):
    '''
    Prepare data for 04 Cross Modal Embeddings project
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
def develop_04_cross_modal_embeddings_model(X, y):
    '''
    Develop 04 Cross Modal Embeddings model for project
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
    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")
    
    return model, y_pred
```

### Step 3: Model Optimization / Bước 3: Tối Ưu Hóa Model
```python
def optimize_04_cross_modal_embeddings_model(X, y):
    '''
    Optimize 04 Cross Modal Embeddings model using hyperparameter tuning
    '''
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import Ridge
    
    # Define parameter grid
    param_grid = {
        'alpha': [0.1, 1.0, 10.0, 100.0],
        'solver': ['auto', 'svd', 'cholesky']
    }
    
    # Grid search
    grid_search = GridSearchCV(
        Ridge(), param_grid, cv=5, scoring='neg_mean_squared_error'
    )
    grid_search.fit(X, y)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {-grid_search.best_score_:.4f}")
    
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

- [Theory](./THEORY_04_cross_modal_embeddings.md)
- [Implementation](./IMPLEMENTATION_04_cross_modal_embeddings.md)
- [Code Examples](./CODE_EXAMPLES_04_cross_modal_embeddings.md)
- [Quiz](./QUIZ_04_cross_modal_embeddings.md)
