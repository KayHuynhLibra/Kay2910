# Smart Contract Security Module

## Overview
Module bảo mật smart contract cung cấp các công cụ và kỹ thuật để bảo vệ và phân tích smart contract trên blockchain.

## Các Kỹ Thuật

### 1. Static Analysis
- **Mô tả**: Phân tích tĩnh
- **Công dụng**: Phát hiện lỗ hổng
- **Tham số**:
  - analysis_method: Phương pháp phân tích
  - rules: Quy tắc kiểm tra
  - output_format: Định dạng kết quả

### 2. Dynamic Analysis
- **Mô tả**: Phân tích động
- **Công dụng**: Kiểm tra thực thi
- **Tham số**:
  - test_method: Phương pháp kiểm thử
  - coverage: Độ phủ
  - timeout: Thời gian chờ

### 3. Formal Verification
- **Mô tả**: Xác minh hình thức
- **Công dụng**: Chứng minh tính đúng đắn
- **Tham số**:
  - verification_method: Phương pháp xác minh
  - properties: Thuộc tính
  - solver: Bộ giải

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import ContractAnalyzer

# Khởi tạo analyzer
analyzer = ContractAnalyzer(contract_path)

# Phân tích contract
results = analyzer.analyze()
```

## Ví dụ

### 1. Phân tích Tĩnh
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import StaticAnalyzer

# Khởi tạo static analyzer
static_analyzer = StaticAnalyzer(
    contract_path="contract.sol",
    analysis_method="slither",
    rules=["reentrancy", "overflow"]
)

# Phân tích contract
results = static_analyzer.analyze()

# Lưu kết quả
static_analyzer.save("static_analysis.json")
```

### 2. Phân tích Động
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import DynamicAnalyzer

# Khởi tạo dynamic analyzer
dynamic_analyzer = DynamicAnalyzer(
    contract_path="contract.sol",
    test_method="fuzzing",
    coverage=0.8
)

# Phân tích contract
results = dynamic_analyzer.analyze()

# Lưu kết quả
dynamic_analyzer.save("dynamic_analysis.json")
```

## Phòng chống

### 1. Formal Verification
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import FormalVerifier

# Khởi tạo verifier
verifier = FormalVerifier(
    contract_path="contract.sol",
    verification_method="model_checking",
    properties=["safety", "liveness"]
)

# Xác minh contract
is_verified = verifier.verify()
```

### 2. Contract Monitoring
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import ContractMonitor

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