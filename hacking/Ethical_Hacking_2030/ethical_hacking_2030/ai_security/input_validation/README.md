# Input Validation Module

## Overview
Module xác thực đầu vào cung cấp các công cụ và kỹ thuật để kiểm tra và xác thực dữ liệu đầu vào cho mô hình AI.

## Các Kỹ Thuật

### 1. Input Sanitization
- **Mô tả**: Làm sạch dữ liệu đầu vào
- **Công dụng**: Loại bỏ dữ liệu độc hại
- **Tham số**:
  - sanitization_method: Phương pháp làm sạch
  - rules: Quy tắc làm sạch
  - threshold: Ngưỡng chấp nhận

### 2. Input Normalization
- **Mô tả**: Chuẩn hóa dữ liệu đầu vào
- **Công dụng**: Đảm bảo tính nhất quán
- **Tham số**:
  - normalization_method: Phương pháp chuẩn hóa
  - range: Khoảng giá trị
  - mean: Giá trị trung bình

### 3. Input Validation
- **Mô tả**: Kiểm tra tính hợp lệ của dữ liệu
- **Công dụng**: Phát hiện dữ liệu bất thường
- **Tham số**:
  - validation_method: Phương pháp kiểm tra
  - rules: Quy tắc kiểm tra
  - threshold: Ngưỡng chấp nhận

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.ai_security.input_validation import InputValidator

# Khởi tạo validator
validator = InputValidator(model)

# Kiểm tra đầu vào
is_valid = validator.validate(input_data)
```

## Ví dụ

### 1. Làm sạch Dữ liệu
```python
from ethical_hacking_2030.ai_security.input_validation import InputSanitizer

# Khởi tạo sanitizer
sanitizer = InputSanitizer(
    sanitization_method="rule_based",
    rules=["remove_special_chars", "normalize_whitespace"]
)

# Làm sạch dữ liệu
clean_data = sanitizer.sanitize(input_data)

# Lưu dữ liệu
sanitizer.save("clean_data.csv")
```

### 2. Chuẩn hóa Dữ liệu
```python
from ethical_hacking_2030.ai_security.input_validation import InputNormalizer

# Khởi tạo normalizer
normalizer = InputNormalizer(
    normalization_method="min_max",
    range=(0, 1)
)

# Chuẩn hóa dữ liệu
normalized_data = normalizer.normalize(input_data)

# Lưu dữ liệu
normalizer.save("normalized_data.npz")
```

## Phòng chống

### 1. Input Validation
```python
from ethical_hacking_2030.ai_security.input_validation import InputValidator

# Khởi tạo validator
validator = InputValidator(
    validation_method="statistical",
    rules=["check_range", "check_distribution"]
)

# Kiểm tra dữ liệu
is_valid = validator.validate(input_data)
```

### 2. Anomaly Detection
```python
from ethical_hacking_2030.ai_security.input_validation import AnomalyDetector

# Khởi tạo detector
detector = AnomalyDetector(
    detection_method="isolation_forest",
    contamination=0.1
)

# Phát hiện bất thường
anomalies = detector.detect(input_data)
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../../../LICENSE) để biết thêm chi tiết. 