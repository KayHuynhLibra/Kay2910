# Blockchain Security Module

## Overview
Module bảo mật Blockchain cung cấp các công cụ và kỹ thuật để bảo vệ hệ thống blockchain và smart contracts khỏi các mối đe dọa bảo mật.

## Cấu trúc Module

### 1. Smart Contract Security
- **Mục tiêu**: Bảo vệ smart contracts
- **Các kỹ thuật**:
  - Static Analysis
  - Dynamic Analysis
  - Formal Verification
- **Công cụ**:
  - Contract Analyzer
  - Vulnerability Scanner
  - Security Checker

### 2. Consensus Security
- **Mục tiêu**: Bảo vệ cơ chế đồng thuận
- **Các kỹ thuật**:
  - Consensus Analysis
  - Attack Prevention
  - Network Security
- **Công cụ**:
  - Consensus Monitor
  - Attack Detector
  - Network Analyzer

### 3. Network Security
- **Mục tiêu**: Bảo vệ mạng blockchain
- **Các kỹ thuật**:
  - P2P Security
  - Node Protection
  - Network Monitoring
- **Công cụ**:
  - Network Monitor
  - Node Security
  - Traffic Analyzer

### 4. Reentrancy Attacks
- **Mục tiêu**: Phát hiện và ngăn chặn tấn công reentrancy
- **Các kỹ thuật**:
  - Pattern Detection
  - Prevention Methods
  - Security Checks
- **Công cụ**:
  - Reentrancy Detector
  - Security Validator
  - Attack Prevention

### 5. Overflow Attacks
- **Mục tiêu**: Phát hiện và ngăn chặn tấn công overflow
- **Các kỹ thuật**:
  - Integer Overflow Detection
  - SafeMath Implementation
  - Security Checks
- **Công cụ**:
  - Overflow Detector
  - Security Validator
  - Attack Prevention

### 6. Access Control
- **Mục tiêu**: Quản lý và kiểm soát truy cập
- **Các kỹ thuật**:
  - Role-based Access Control
  - Permission Management
  - Security Policies
- **Công cụ**:
  - Access Controller
  - Permission Manager
  - Policy Enforcer

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.blockchain_security import smart_contract_security

# Phân tích smart contract
analyzer = smart_contract_security.ContractAnalyzer()
results = analyzer.analyze(contract_address)

# Kiểm tra bảo mật
security_checker = smart_contract_security.SecurityChecker()
vulnerabilities = security_checker.check(contract_address)
```

## Ví dụ

### 1. Phân tích Smart Contract
```python
from ethical_hacking_2030.blockchain_security.smart_contract_security import ContractAnalyzer

# Khởi tạo analyzer
analyzer = ContractAnalyzer()

# Phân tích contract
results = analyzer.analyze("0x123...")

# In kết quả
print(results.get_vulnerabilities())
```

### 2. Kiểm tra Reentrancy
```python
from ethical_hacking_2030.blockchain_security.reentrancy_attacks import ReentrancyDetector

# Khởi tạo detector
detector = ReentrancyDetector()

# Kiểm tra contract
vulnerabilities = detector.check_contract(contract_address)

# In kết quả
print(vulnerabilities.get_reentrancy_issues())
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../LICENSE) để biết thêm chi tiết. 