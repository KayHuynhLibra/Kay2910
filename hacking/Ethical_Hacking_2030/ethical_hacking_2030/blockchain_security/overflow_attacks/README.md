# Overflow Attacks Module

## Overview
Module tấn công overflow cung cấp các công cụ và kỹ thuật để phát hiện và phòng chống tấn công tràn số trong smart contract.

## Các Kỹ Thuật

### 1. Integer Overflow Detection
- **Mô tả**: Phát hiện tràn số nguyên
- **Công dụng**: Nhận diện lỗ hổng
- **Tham số**:
  - detection_method: Phương pháp phát hiện
  - data_types: Kiểu dữ liệu
  - sensitivity: Độ nhạy

### 2. SafeMath Implementation
- **Mô tả**: Triển khai SafeMath
- **Công dụng**: Ngăn chặn tràn số
- **Tham số**:
  - operations: Phép toán
  - validation: Xác thực
  - error_handling: Xử lý lỗi

### 3. Security Checks
- **Mô tả**: Kiểm tra bảo mật
- **Công dụng**: Xác minh an toàn
- **Tham số**:
  - check_types: Loại kiểm tra
  - rules: Quy tắc
  - thresholds: Ngưỡng

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.blockchain_security.overflow_attacks import OverflowDetector

# Khởi tạo detector
detector = OverflowDetector(contract_path)

# Phát hiện lỗ hổng
results = detector.detect()
```

## Ví dụ

### 1. Integer Overflow Detection
```python
from ethical_hacking_2030.blockchain_security.overflow_attacks import IntegerOverflowDetector

# Khởi tạo detector
overflow_detector = IntegerOverflowDetector(
    contract_path="contract.sol",
    detection_method="static_analysis",
    data_types=["uint256", "int256"]
)

# Phát hiện tràn số
results = overflow_detector.detect()

# Lưu kết quả
overflow_detector.save("overflow_detection.json")
```

### 2. SafeMath Implementation
```python
from ethical_hacking_2030.blockchain_security.overflow_attacks import SafeMath

# Khởi tạo SafeMath
safe_math = SafeMath(
    operations=["add", "sub", "mul", "div"],
    validation=True,
    error_handling="revert"
)

# Triển khai SafeMath
safe_math.implement()
```

## Phòng chống

### 1. Security Validation
```python
from ethical_hacking_2030.blockchain_security.overflow_attacks import SecurityValidator

# Khởi tạo validator
validator = SecurityValidator(
    contract_path="contract.sol",
    check_types=["integer_overflow", "safe_math"],
    rules=["use_safemath", "validate_inputs"]
)

# Kiểm tra bảo mật
is_secure = validator.validate()
```

### 2. Contract Monitoring
```python
from ethical_hacking_2030.blockchain_security.overflow_attacks import ContractMonitor

# Khởi tạo monitor
monitor = ContractMonitor(
    contract_address="0x123...",
    monitoring_method="continuous"
)

# Giám sát contract
monitor.start_monitoring()
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../../../LICENSE) để biết thêm chi tiết. 