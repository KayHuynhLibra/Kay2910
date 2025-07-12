# Reentrancy Attacks Module

## Overview
Module tấn công reentrancy cung cấp các công cụ và kỹ thuật để phát hiện và phòng chống tấn công reentrancy trong smart contract.

## Các Kỹ Thuật

### 1. Pattern Detection
- **Mô tả**: Phát hiện mẫu tấn công
- **Công dụng**: Nhận diện lỗ hổng
- **Tham số**:
  - patterns: Mẫu tấn công
  - detection_method: Phương pháp phát hiện
  - sensitivity: Độ nhạy

### 2. Prevention Methods
- **Mô tả**: Phương pháp phòng chống
- **Công dụng**: Ngăn chặn tấn công
- **Tham số**:
  - prevention_type: Loại phòng chống
  - implementation: Cách triển khai
  - validation: Xác thực

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
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import ReentrancyDetector

# Khởi tạo detector
detector = ReentrancyDetector(contract_path)

# Phát hiện lỗ hổng
results = detector.detect()
```

## Ví dụ

### 1. Pattern Detection
```python
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import PatternDetector

# Khởi tạo pattern detector
pattern_detector = PatternDetector(
    contract_path="contract.sol",
    patterns=["external_call", "state_change"],
    detection_method="static_analysis"
)

# Phát hiện mẫu
results = pattern_detector.detect()

# Lưu kết quả
pattern_detector.save("pattern_detection.json")
```

### 2. Prevention Implementation
```python
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import PreventionSystem

# Khởi tạo prevention system
prevention = PreventionSystem(
    prevention_type="checks_effects_interactions",
    implementation="modifier",
    validation=True
)

# Triển khai phòng chống
prevention.implement()
```

## Phòng chống

### 1. Security Validation
```python
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import SecurityValidator

# Khởi tạo validator
validator = SecurityValidator(
    contract_path="contract.sol",
    check_types=["reentrancy", "state_management"],
    rules=["checks_effects_interactions"]
)

# Kiểm tra bảo mật
is_secure = validator.validate()
```

### 2. Contract Monitoring
```python
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import ContractMonitor

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