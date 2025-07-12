#!/usr/bin/env python3
"""
Complete System Enhancement Script
Bổ sung 4 loại file còn thiếu cho tất cả 20 chủ đề chính:
1. Accuracy Analysis
2. Mathematical Foundation  
3. Validation Framework
4. Research Methodology
"""

import os
from pathlib import Path

def create_accuracy_analysis_file(folder_path, topic_name):
    """Tạo file phân tích tính chính xác"""
    content = f"""# 🎯 Phân Tích Tính Chính Xác - {topic_name}

## 📊 Metrics Đánh Giá Chính

### 1. **Classification Metrics**
- **Accuracy**: Độ chính xác tổng thể
- **Precision**: Độ chính xác dương tính
- **Recall**: Độ bao phủ dương tính  
- **F1-Score**: Trung bình điều hòa của Precision và Recall
- **ROC-AUC**: Diện tích dưới đường cong ROC
- **PR-AUC**: Diện tích dưới đường cong Precision-Recall
- **Balanced Accuracy**: Độ chính xác cân bằng
- **Cohen's Kappa**: Hệ số Kappa
- **Matthews Correlation**: Hệ số tương quan Matthews

### 2. **Regression Metrics**
- **RMSE**: Root Mean Square Error
- **MAE**: Mean Absolute Error
- **MAPE**: Mean Absolute Percentage Error
- **R²**: Coefficient of Determination
- **Adjusted R²**: R² điều chỉnh cho số features
- **Explained Variance Score**: Tỷ lệ phương sai được giải thích

### 3. **Clustering Metrics**
- **Silhouette Score**: Độ tương đồng trong cluster
- **Calinski-Harabasz Index**: Tỷ lệ dispersion
- **Davies-Bouldin Index**: Độ compact của clusters
- **Inertia**: Tổng khoảng cách bình phương

## 🔍 Phân Tích Chi Tiết

### Bias-Variance Tradeoff
```python
import numpy as np
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

def analyze_bias_variance(model, X, y):
    train_sizes, train_scores, val_scores = learning_curve(
        model, X, y, cv=5, n_jobs=-1, 
        train_sizes=np.linspace(0.1, 1.0, 10)
    )
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, label='Training score')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
    plt.plot(train_sizes, val_mean, label='Cross-validation score')
    plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1)
    plt.xlabel('Training Examples')
    plt.ylabel('Score')
    plt.title('Learning Curves')
    plt.legend()
    plt.grid(True)
    plt.show()
```

### Confidence Intervals
```python
from scipy import stats

def calculate_confidence_interval(predictions, confidence=0.95):
    mean = np.mean(predictions)
    std = np.std(predictions)
    n = len(predictions)
    
    t_value = stats.t.ppf((1 + confidence) / 2, n - 1)
    margin = t_value * (std / np.sqrt(n))
    
    return mean - margin, mean + margin
```

### Statistical Significance Testing
```python
from scipy.stats import ttest_ind, mannwhitneyu

def compare_models(model1_scores, model2_scores, alpha=0.05):
    t_stat, p_value = ttest_ind(model1_scores, model2_scores)
    u_stat, u_p_value = mannwhitneyu(model1_scores, model2_scores)
    
    print(f"T-test p-value: {p_value:.4f}")
    print(f"Mann-Whitney U test p-value: {u_p_value:.4f}")
    
    if p_value < alpha:
        print("Có sự khác biệt có ý nghĩa thống kê (T-test)")
    else:
        print("Không có sự khác biệt có ý nghĩa thống kê (T-test)")
```

## 📈 Visualization Tools

### Confusion Matrix
```python
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, labels=None):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
```

### ROC Curve
```python
from sklearn.metrics import roc_curve, auc

def plot_roc_curve(y_true, y_pred_proba):
    fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
             label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()
```

### Residual Analysis
```python
def plot_residuals(y_true, y_pred):
    residuals = y_true - y_pred
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Residuals vs Predicted
    axes[0, 0].scatter(y_pred, residuals)
    axes[0, 0].axhline(y=0, color='r', linestyle='--')
    axes[0, 0].set_xlabel('Predicted Values')
    axes[0, 0].set_ylabel('Residuals')
    axes[0, 0].set_title('Residuals vs Predicted')
    
    # Q-Q Plot
    from scipy import stats
    stats.probplot(residuals, dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title('Q-Q Plot')
    
    # Histogram of residuals
    axes[1, 0].hist(residuals, bins=30, alpha=0.7)
    axes[1, 0].set_xlabel('Residuals')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Histogram of Residuals')
    
    # Residuals vs Index
    axes[1, 1].plot(residuals)
    axes[1, 1].axhline(y=0, color='r', linestyle='--')
    axes[1, 1].set_xlabel('Index')
    axes[1, 1].set_ylabel('Residuals')
    axes[1, 1].set_title('Residuals vs Index')
    
    plt.tight_layout()
    plt.show()
```

## 🎯 Best Practices

### 1. **Cross-Validation Strategy**
- Sử dụng stratified k-fold cho classification
- Time series split cho dữ liệu thời gian
- Nested cross-validation cho hyperparameter tuning

### 2. **Multiple Metrics**
- Không chỉ dựa vào một metric
- Cân nhắc business context
- Trade-off giữa precision và recall

### 3. **Statistical Rigor**
- Kiểm tra statistical significance
- Confidence intervals
- Effect size analysis

### 4. **Reproducibility**
- Set random seeds
- Document preprocessing steps
- Version control cho code và data

## 📊 Reporting Template

### Model Performance Report
```python
def generate_performance_report(model, X_test, y_test, y_pred):
    from sklearn.metrics import classification_report, accuracy_score
    
    report = {{
        'accuracy': accuracy_score(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()
    }}
    
    return report
```

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_01_{topic_name.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_01_{topic_name.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Quiz](./QUIZ_01_{topic_name.lower().replace(' ', '_')}.md)
- [Project](./PROJECT_01_{topic_name.lower().replace(' ', '_')}.md)
"""
    
    file_path = folder_path / f"ACCURACY_ANALYSIS_01_{topic_name.lower().replace(' ', '_')}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def create_mathematical_foundation_file(folder_path, topic_name):
    """Tạo file nền tảng toán học chi tiết"""
    content = f"""# 🧮 Nền Tảng Toán Học Chi Tiết - {topic_name}

## 📐 Mathematical Foundations

### 1. **Linear Algebra Fundamentals**

#### Vector Operations
```python
import numpy as np

def vector_addition(v1, v2):
    return v1 + v2

def dot_product(v1, v2):
    return np.dot(v1, v2)

def vector_norm(v, p=2):
    return np.linalg.norm(v, ord=p)

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
```

#### Matrix Operations
```python
def matrix_multiply(A, B):
    return np.matmul(A, B)

def matrix_inverse(A):
    return np.linalg.inv(A)

def eigendecomposition(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

def svd_decomposition(A):
    U, S, Vt = np.linalg.svd(A)
    return U, S, Vt
```

### 2. **Calculus Essentials**

#### Derivatives
```python
import sympy as sp

def symbolic_derivative(expression, variable):
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)
    return sp.diff(expr, x)

def numerical_gradient(f, x, h=1e-7):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += h
        x_minus[i] -= h
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
    return grad
```

#### Optimization
```python
def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iter=1000):
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = grad_f(x)
        x = x - learning_rate * grad
        history.append(x.copy())
        
        if np.linalg.norm(grad) < 1e-6:
            break
    
    return x, history

def newton_method(f, grad_f, hess_f, x0, max_iter=100):
    x = x0.copy()
    
    for i in range(max_iter):
        grad = grad_f(x)
        hess = hess_f(x)
        
        if np.linalg.det(hess) == 0:
            break
            
        x = x - np.linalg.solve(hess, grad)
        
        if np.linalg.norm(grad) < 1e-6:
            break
    
    return x
```

### 3. **Probability & Statistics**

#### Probability Distributions
```python
from scipy import stats

def normal_distribution_example():
    mu, sigma = 0, 1
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    
    plt.plot(x, y)
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.show()

def bayesian_inference_example():
    prior_mean = 0
    prior_std = 1
    data = np.random.normal(2, 0.5, 100)
    
    n = len(data)
    posterior_mean = (prior_mean / prior_std**2 + np.sum(data) / 0.5**2) / \
                     (1 / prior_std**2 + n / 0.5**2)
    posterior_std = np.sqrt(1 / (1 / prior_std**2 + n / 0.5**2))
    
    return posterior_mean, posterior_std
```

#### Statistical Tests
```python
def hypothesis_testing(data, null_hypothesis, alpha=0.05):
    # T-test
    t_stat, p_value = stats.ttest_1samp(data, null_hypothesis)
    
    # Chi-square test
    chi2_stat, chi2_p_value = stats.chisquare(data)
    
    return {{
        't_test': {{'statistic': t_stat, 'p_value': p_value}},
        'chi2_test': {{'statistic': chi2_stat, 'p_value': chi2_p_value}}
    }}
```

### 4. **Information Theory**

#### Entropy and Information
```python
def entropy(probabilities):
    probabilities = np.array(probabilities)
    probabilities = probabilities[probabilities > 0]
    return -np.sum(probabilities * np.log2(probabilities))

def mutual_information(X, Y):
    joint_dist = np.histogram2d(X, Y, bins=20)[0]
    joint_dist = joint_dist / np.sum(joint_dist)
    
    p_x = np.sum(joint_dist, axis=1)
    p_y = np.sum(joint_dist, axis=0)
    
    mi = 0
    for i in range(joint_dist.shape[0]):
        for j in range(joint_dist.shape[1]):
            if joint_dist[i, j] > 0:
                mi += joint_dist[i, j] * np.log2(
                    joint_dist[i, j] / (p_x[i] * p_y[j])
                )
    
    return mi

def kl_divergence(p, q):
    p = np.array(p)
    q = np.array(q)
    
    # Avoid division by zero
    q = np.where(q == 0, 1e-10, q)
    
    return np.sum(p * np.log(p / q))
```

### 5. **Advanced Mathematical Concepts**

#### Functional Analysis
```python
def functional_norm(f, domain, p=2):
    x = np.linspace(domain[0], domain[1], 1000)
    y = f(x)
    return np.linalg.norm(y, ord=p)

def fourier_transform(signal, sample_rate):
    from scipy.fft import fft
    fft_result = fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1/sample_rate)
    return frequencies, fft_result
```

#### Measure Theory
```python
def lebesgue_integral(f, domain, measure_func=None):
    if measure_func is None:
        measure_func = lambda x: 1
    
    x = np.linspace(domain[0], domain[1], 1000)
    y = f(x)
    measure = measure_func(x)
    
    return np.trapz(y * measure, x)
```

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_01_{topic_name.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_01_{topic_name.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Accuracy Analysis](./ACCURACY_ANALYSIS_01_{topic_name.lower().replace(' ', '_')}.md)
"""
    
    file_path = folder_path / f"MATHEMATICAL_FOUNDATION_01_{topic_name.lower().replace(' ', '_')}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def create_validation_framework_file(folder_path, topic_name):
    """Tạo framework validation chi tiết"""
    content = f"""# ✅ Framework Validation Chi Tiết - {topic_name}

## 🎯 Validation Strategy

### 1. **Data Validation**

#### Data Quality Checks
```python
import pandas as pd
import numpy as np
from scipy import stats

def comprehensive_data_validation(df):
    validation_report = {{
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes.to_dict(),
        'outliers': {{}},
        'correlations': {{}},
        'distributions': {{}}
    }}
    
    # Outlier detection
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
        validation_report['outliers'][col] = len(outliers)
    
    # Correlation analysis
    correlation_matrix = df.corr()
    validation_report['correlations'] = correlation_matrix.to_dict()
    
    return validation_report
```

#### Statistical Tests
```python
def statistical_validation(data, alpha=0.05):
    tests = {{}}
    
    # Normality test
    if len(data) > 3:
        stat, p_value = stats.normaltest(data)
        tests['normality'] = {{
            'statistic': stat,
            'p_value': p_value,
            'is_normal': p_value > alpha
        }}
    
    # Stationarity test (for time series)
    if len(data) > 50:
        from statsmodels.tsa.stattools import adfuller
        adf_result = adfuller(data)
        tests['stationarity'] = {{
            'adf_statistic': adf_result[0],
            'p_value': adf_result[1],
            'is_stationary': adf_result[1] < alpha
        }}
    
    return tests
```

### 2. **Model Validation**

#### Cross-Validation Framework
```python
from sklearn.model_selection import (
    KFold, StratifiedKFold, TimeSeriesSplit, 
    cross_val_score, cross_validate
)

def comprehensive_cross_validation(model, X, y, cv_strategy='stratified'):
    if cv_strategy == 'stratified':
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    elif cv_strategy == 'time_series':
        cv = TimeSeriesSplit(n_splits=5)
    else:
        cv = KFold(n_splits=5, shuffle=True, random_state=42)
    
    scoring = {{
        'accuracy': 'accuracy',
        'precision': 'precision_macro',
        'recall': 'recall_macro',
        'f1': 'f1_macro',
        'roc_auc': 'roc_auc_ovr'
    }}
    
    results = cross_validate(model, X, y, cv=cv, scoring=scoring, 
                           return_train_score=True)
    
    return results
```

#### Bootstrap Validation
```python
def bootstrap_validation(model, X, y, n_bootstrap=1000):
    n_samples = len(X)
    bootstrap_scores = []
    
    for _ in range(n_bootstrap):
        indices = np.random.choice(n_samples, n_samples, replace=True)
        X_boot, y_boot = X[indices], y[indices]
        
        model.fit(X_boot, y_boot)
        score = model.score(X, y)
        bootstrap_scores.append(score)
    
    alpha = 0.05
    lower_percentile = (alpha / 2) * 100
    upper_percentile = (1 - alpha / 2) * 100
    
    ci_lower = np.percentile(bootstrap_scores, lower_percentile)
    ci_upper = np.percentile(bootstrap_scores, upper_percentile)
    
    return {{
        'mean_score': np.mean(bootstrap_scores),
        'std_score': np.std(bootstrap_scores),
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'bootstrap_scores': bootstrap_scores
    }}
```

### 3. **Performance Validation**

#### Model Comparison Framework
```python
def model_comparison_framework(models, X, y, cv=5):
    comparison_results = {{}}
    
    for name, model in models.items():
        cv_scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
        bootstrap_results = bootstrap_validation(model, X, y)
        
        comparison_results[name] = {{
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'bootstrap_mean': bootstrap_results['mean_score'],
            'bootstrap_ci': (bootstrap_results['ci_lower'], 
                           bootstrap_results['ci_upper'])
        }}
    
    return comparison_results
```

#### Statistical Significance Testing
```python
from scipy.stats import friedmanchisquare, wilcoxon

def statistical_comparison(model_scores_dict):
    model_names = list(model_scores_dict.keys())
    scores_matrix = np.array([model_scores_dict[name] for name in model_names])
    
    # Friedman test
    friedman_stat, friedman_p_value = friedmanchisquare(*scores_matrix)
    
    # Pairwise Wilcoxon tests
    pairwise_results = {{}}
    for i in range(len(model_names)):
        for j in range(i+1, len(model_names)):
            wilcoxon_stat, wilcoxon_p_value = wilcoxon(scores_matrix[i], scores_matrix[j])
            pairwise_results[f"{{model_names[i]}} vs {{model_names[j]}}"] = {{
                'statistic': wilcoxon_stat,
                'p_value': wilcoxon_p_value
            }}
    
    return {{
        'friedman_test': {{'statistic': friedman_stat, 'p_value': friedman_p_value}},
        'pairwise_tests': pairwise_results
    }}
```

### 4. **Business Validation**

#### ROI Analysis
```python
def roi_analysis(model_performance, business_metrics):
    roi_calculation = {{
        'accuracy_improvement': model_performance['accuracy'] - business_metrics['baseline_accuracy'],
        'cost_savings': business_metrics['cost_per_error'] * model_performance['error_reduction'],
        'revenue_increase': business_metrics['revenue_per_correct_prediction'] * model_performance['correct_predictions'],
        'implementation_cost': business_metrics['implementation_cost']
    }}
    
    roi_calculation['net_benefit'] = (
        roi_calculation['cost_savings'] + 
        roi_calculation['revenue_increase'] - 
        roi_calculation['implementation_cost']
    )
    
    roi_calculation['roi_percentage'] = (
        roi_calculation['net_benefit'] / roi_calculation['implementation_cost']
    ) * 100
    
    return roi_calculation
```

#### A/B Testing Framework
```python
def ab_testing_framework(control_group, treatment_group, alpha=0.05):
    from scipy.stats import ttest_ind, chi2_contingency
    
    if isinstance(control_group[0], (int, float)):
        stat, p_value = ttest_ind(control_group, treatment_group)
        test_type = 't-test'
    else:
        contingency_table = pd.crosstab(
            control_group + treatment_group,
            ['control'] * len(control_group) + ['treatment'] * len(treatment_group)
        )
        stat, p_value, _, _ = chi2_contingency(contingency_table)
        test_type = 'chi-square'
    
    return {{
        'test_type': test_type,
        'statistic': stat,
        'p_value': p_value,
        'significant': p_value < alpha,
        'effect_size': abs(stat)
    }}
```

## 📊 Validation Reporting

### Comprehensive Report Template
```python
def generate_validation_report(model, X, y, business_context=None):
    report = {{
        'data_validation': comprehensive_data_validation(pd.DataFrame(X)),
        'model_validation': comprehensive_cross_validation(model, X, y),
        'bootstrap_validation': bootstrap_validation(model, X, y),
        'statistical_tests': statistical_validation(y)
    }}
    
    if business_context:
        report['business_validation'] = roi_analysis(
            report['model_validation'], business_context
        )
    
    return report
```

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_01_{topic_name.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_01_{topic_name.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Accuracy Analysis](./ACCURACY_ANALYSIS_01_{topic_name.lower().replace(' ', '_')}.md)
- [Mathematical Foundation](./MATHEMATICAL_FOUNDATION_01_{topic_name.lower().replace(' ', '_')}.md)
"""
    
    file_path = folder_path / f"VALIDATION_FRAMEWORK_01_{topic_name.lower().replace(' ', '_')}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def create_research_methodology_file(folder_path, topic_name):
    """Tạo file phương pháp nghiên cứu"""
    content = f"""# 🔬 Phương Pháp Nghiên Cứu - {topic_name}

## 📋 Research Methodology Framework

### 1. **Research Design**

#### Experimental Design
```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def factorial_design(factors, levels):
    from itertools import product
    
    combinations = list(product(*levels))
    
    design_matrix = []
    for combo in combinations:
        design_matrix.append(dict(zip(factors, combo)))
    
    return design_matrix

def randomized_controlled_trial(control_group, treatment_group, alpha=0.05):
    np.random.shuffle(control_group)
    np.random.shuffle(treatment_group)
    
    stat, p_value = stats.ttest_ind(control_group, treatment_group)
    
    return {{
        'statistic': stat,
        'p_value': p_value,
        'significant': p_value < alpha,
        'effect_size': abs(stat)
    }}
```

#### Sampling Methods
```python
def stratified_sampling(data, strata_column, sample_size):
    stratified_sample = []
    
    for stratum in data[strata_column].unique():
        stratum_data = data[data[strata_column] == stratum]
        stratum_sample = stratum_data.sample(
            n=min(sample_size, len(stratum_data)), 
            random_state=42
        )
        stratified_sample.append(stratum_sample)
    
    return pd.concat(stratified_sample)

def systematic_sampling(data, step_size):
    indices = range(0, len(data), step_size)
    return data.iloc[indices]
```

### 2. **Data Collection Methods**

#### Survey Design
```python
def survey_validation(survey_data):
    validation_metrics = {{
        'completion_rate': len(survey_data.dropna()) / len(survey_data),
        'response_rate': len(survey_data) / survey_data['invited_count'].sum(),
        'internal_consistency': calculate_cronbach_alpha(survey_data),
        'test_retest_reliability': calculate_test_retest(survey_data)
    }}
    
    return validation_metrics

def calculate_cronbach_alpha(data):
    n_items = data.shape[1]
    item_variances = data.var()
    total_variance = data.sum(axis=1).var()
    
    alpha = (n_items / (n_items - 1)) * (1 - item_variances.sum() / total_variance)
    return alpha
```

#### Experimental Protocols
```python
def experimental_protocol(participants, conditions, measurements):
    protocol = {{
        'participants': {{
            'sample_size': len(participants),
            'inclusion_criteria': ['age >= 18', 'no prior experience'],
            'exclusion_criteria': ['cognitive impairment', 'language barriers']
        }},
        'conditions': conditions,
        'measurements': measurements,
        'randomization': 'blocked_randomization',
        'blinding': 'double_blind'
    }}
    
    return protocol
```

### 3. **Statistical Analysis**

#### Hypothesis Testing Framework
```python
def hypothesis_testing_framework(data, null_hypothesis, alternative_hypothesis, alpha=0.05):
    if len(data) > 30:
        if len(data) == 2:
            stat, p_value = stats.ttest_ind(data[0], data[1])
            test_type = 'Independent t-test'
        else:
            stat, p_value = stats.f_oneway(*data)
            test_type = 'ANOVA'
    else:
        if len(data) == 2:
            stat, p_value = stats.mannwhitneyu(data[0], data[1])
            test_type = 'Mann-Whitney U test'
        else:
            stat, p_value = stats.kruskal(*data)
            test_type = 'Kruskal-Wallis test'
    
    return {{
        'test_type': test_type,
        'statistic': stat,
        'p_value': p_value,
        'significant': p_value < alpha,
        'null_hypothesis': null_hypothesis,
        'alternative_hypothesis': alternative_hypothesis,
        'conclusion': 'Reject H0' if p_value < alpha else 'Fail to reject H0'
    }}
```

#### Effect Size Analysis
```python
def effect_size_analysis(group1, group2):
    pooled_std = np.sqrt(((len(group1) - 1) * np.var(group1) + 
                         (len(group2) - 1) * np.var(group2)) / 
                        (len(group1) + len(group2) - 2))
    
    cohens_d = (np.mean(group1) - np.mean(group2)) / pooled_std
    
    if abs(cohens_d) < 0.2:
        effect_size = 'Small'
    elif abs(cohens_d) < 0.5:
        effect_size = 'Medium'
    else:
        effect_size = 'Large'
    
    return {{
        'cohens_d': cohens_d,
        'effect_size': effect_size,
        'interpretation': f'{{effect_size}} effect size'
    }}
```

### 4. **Research Ethics**

#### Ethical Considerations
```python
def ethical_framework():
    ethical_guidelines = {{
        'informed_consent': {{
            'required': True,
            'description': 'Participants must provide informed consent',
            'implementation': 'Written consent form with clear explanation'
        }},
        'privacy_protection': {{
            'required': True,
            'description': 'Protect participant privacy and confidentiality',
            'implementation': 'Data anonymization and secure storage'
        }},
        'beneficence': {{
            'required': True,
            'description': 'Maximize benefits and minimize harms',
            'implementation': 'Risk-benefit analysis and monitoring'
        }},
        'justice': {{
            'required': True,
            'description': 'Fair distribution of benefits and burdens',
            'implementation': 'Inclusive sampling and fair treatment'
        }}
    }}
    
    return ethical_guidelines
```

#### Data Privacy Compliance
```python
def privacy_compliance_check(data, regulations=['GDPR', 'CCPA']):
    compliance_report = {{}}
    
    for regulation in regulations:
        if regulation == 'GDPR':
            compliance_report[regulation] = {{
                'data_minimization': check_data_minimization(data),
                'purpose_limitation': check_purpose_limitation(data),
                'storage_limitation': check_storage_limitation(data),
                'right_to_erasure': check_right_to_erasure(data)
            }}
        elif regulation == 'CCPA':
            compliance_report[regulation] = {{
                'right_to_know': check_right_to_know(data),
                'right_to_delete': check_right_to_delete(data),
                'right_to_opt_out': check_right_to_opt_out(data)
            }}
    
    return compliance_report
```

### 5. **Research Reporting**

#### Publication Standards
```python
def research_report_template():
    report_structure = {{
        'abstract': {{
            'background': 'Brief background and context',
            'methods': 'Study design and methodology',
            'results': 'Key findings and outcomes',
            'conclusion': 'Main conclusions and implications'
        }},
        'introduction': {{
            'problem_statement': 'Clear problem definition',
            'literature_review': 'Review of relevant research',
            'research_questions': 'Specific research questions',
            'hypotheses': 'Testable hypotheses'
        }},
        'methods': {{
            'participants': 'Sample description and recruitment',
            'materials': 'Tools and instruments used',
            'procedure': 'Detailed experimental procedure',
            'analysis': 'Statistical analysis plan'
        }},
        'results': {{
            'descriptive_statistics': 'Summary statistics',
            'inferential_statistics': 'Hypothesis testing results',
            'effect_sizes': 'Effect size calculations',
            'assumptions': 'Test of statistical assumptions'
        }},
        'discussion': {{
            'interpretation': 'Interpretation of results',
            'limitations': 'Study limitations',
            'implications': 'Practical and theoretical implications',
            'future_research': 'Directions for future research'
        }}
    }}
    
    return report_structure
```

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_01_{topic_name.lower().replace(' ', '_')}.md)
- [Implementation](./IMPLEMENTATION_01_{topic_name.lower().replace(' ', '_')}.md)
- [Code Examples](./CODE_EXAMPLES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Best Practices](./BEST_PRACTICES_01_{topic_name.lower().replace(' ', '_')}.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
- [Accuracy Analysis](./ACCURACY_ANALYSIS_01_{topic_name.lower().replace(' ', '_')}.md)
- [Mathematical Foundation](./MATHEMATICAL_FOUNDATION_01_{topic_name.lower().replace(' ', '_')}.md)
- [Validation Framework](./VALIDATION_FRAMEWORK_01_{topic_name.lower().replace(' ', '_')}.md)
"""
    
    file_path = folder_path / f"RESEARCH_METHODOLOGY_01_{topic_name.lower().replace(' ', '_')}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def enhance_all_topics():
    """Bổ sung tất cả 4 loại file cho tất cả 20 chủ đề chính"""
    
    # Các thư mục chính
    main_folders = [
        "01_Machine_Learning",
        "02_Deep_Learning", 
        "03_Neural_Networks",
        "04_Natural_Language_Processing",
        "05_Computer_Vision",
        "06_Reinforcement_Learning",
        "07_Generative_Models",
        "08_Large_Language_Models",
        "09_Transformers",
        "10_Feature_Engineering",
        "11_Supervised_Learning",
        "12_Bayesian_Learning",
        "13_Prompt_Engineering",
        "14_AI_Agents",
        "15_Fine_tuning_Models",
        "16_Multimodal_Models",
        "17_Embeddings",
        "18_Vector_Search",
        "19_Model_Evaluation",
        "20_AI_Infrastructure"
    ]
    
    enhanced_files = []
    
    for folder in main_folders:
        folder_path = Path(folder)
        if folder_path.exists():
            # Lấy tên chủ đề từ tên thư mục
            topic_name = folder.replace('_', ' ').replace('01 ', '').replace('02 ', '').replace('03 ', '').replace('04 ', '').replace('05 ', '').replace('06 ', '').replace('07 ', '').replace('08 ', '').replace('09 ', '').replace('10 ', '').replace('11 ', '').replace('12 ', '').replace('13 ', '').replace('14 ', '').replace('15 ', '').replace('16 ', '').replace('17 ', '').replace('18 ', '').replace('19 ', '').replace('20 ', '')
            
            print(f"🔧 Bổ sung cho: {topic_name}")
            
            try:
                # 1. Accuracy Analysis
                accuracy_file = create_accuracy_analysis_file(folder_path, topic_name)
                enhanced_files.append(accuracy_file)
                print(f"  ✅ Tạo: {accuracy_file.name}")
                
                # 2. Mathematical Foundation
                math_file = create_mathematical_foundation_file(folder_path, topic_name)
                enhanced_files.append(math_file)
                print(f"  ✅ Tạo: {math_file.name}")
                
                # 3. Validation Framework
                validation_file = create_validation_framework_file(folder_path, topic_name)
                enhanced_files.append(validation_file)
                print(f"  ✅ Tạo: {validation_file.name}")
                
                # 4. Research Methodology
                research_file = create_research_methodology_file(folder_path, topic_name)
                enhanced_files.append(research_file)
                print(f"  ✅ Tạo: {research_file.name}")
                
            except Exception as e:
                print(f"  ❌ Lỗi khi tạo file cho {topic_name}: {e}")
    
    return enhanced_files

if __name__ == "__main__":
    print("🚀 Bắt đầu bổ sung tính đầy đủ cho hệ thống AI/ML...")
    print("=" * 60)
    
    enhanced_files = enhance_all_topics()
    
    print("\n" + "=" * 60)
    print(f"🎉 Hoàn thành! Đã tạo {len(enhanced_files)} file bổ sung")
    print("\n📋 Tóm tắt các thành phần đã bổ sung:")
    print("1. 📊 Accuracy Analysis - Phân tích tính chính xác chi tiết")
    print("2. 🧮 Mathematical Foundation - Nền tảng toán học")
    print("3. ✅ Validation Framework - Framework validation toàn diện")
    print("4. 🔬 Research Methodology - Phương pháp nghiên cứu")
    
    print("\n🎯 Hệ thống hiện tại đã đầy đủ từ lý thuyết đến tính chính xác!")
    print("   - Lý thuyết cơ bản và nâng cao")
    print("   - Implementation chi tiết")
    print("   - Code examples thực tế")
    print("   - Best practices")
    print("   - Complex problems")
    print("   - Accuracy analysis")
    print("   - Mathematical foundation")
    print("   - Validation framework")
    print("   - Research methodology") 