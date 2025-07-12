# Access Control Module

## Overview
Module kiểm soát truy cập cung cấp các công cụ và kỹ thuật để quản lý và bảo vệ quyền truy cập trong smart contract.

## Các Kỹ Thuật

### 1. Role-based Access Control
- **Mô tả**: Kiểm soát truy cập dựa trên vai trò
- **Công dụng**: Phân quyền người dùng
- **Tham số**:
  - roles: Vai trò
  - permissions: Quyền hạn
  - inheritance: Kế thừa

### 2. Permission Management
- **Mô tả**: Quản lý quyền hạn
- **Công dụng**: Kiểm soát quyền
- **Tham số**:
  - permission_types: Loại quyền
  - assignment: Phân gán
  - validation: Xác thực

### 3. Security Policies
- **Mô tả**: Chính sách bảo mật
- **Công dụng**: Quy định bảo mật
- **Tham số**:
  - policy_types: Loại chính sách
  - rules: Quy tắc
  - enforcement: Thực thi

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.blockchain_security.access_control import AccessController

# Khởi tạo controller
controller = AccessController(contract_path)

# Kiểm tra quyền
has_access = controller.check_access(user_address, role)
```

## Ví dụ

### 1. Role-based Access Control
```python
from ethical_hacking_2030.blockchain_security.access_control import RBAC

# Khởi tạo RBAC
rbac = RBAC(
    roles=["admin", "user", "guest"],
    permissions={
        "admin": ["read", "write", "delete"],
        "user": ["read", "write"],
        "guest": ["read"]
    }
)

# Phân quyền
rbac.assign_role(user_address, "admin")
```

### 2. Permission Management
```python
from ethical_hacking_2030.blockchain_security.access_control import PermissionManager

# Khởi tạo permission manager
permission_manager = PermissionManager(
    permission_types=["read", "write", "delete"],
    assignment_method="role_based",
    validation=True
)

# Quản lý quyền
permission_manager.grant_permission(user_address, "write")
```

## Phòng chống

### 1. Security Validation
```python
from ethical_hacking_2030.blockchain_security.access_control import SecurityValidator

# Khởi tạo validator
validator = SecurityValidator(
    contract_path="contract.sol",
    check_types=["access_control", "permissions"],
    rules=["least_privilege", "separation_of_duties"]
)

# Kiểm tra bảo mật
is_secure = validator.validate()
```

### 2. Access Monitoring
```python
from ethical_hacking_2030.blockchain_security.access_control import AccessMonitor

# Khởi tạo monitor
monitor = AccessMonitor(
    contract_address="0x123...",
    monitoring_method="continuous"
)

# Giám sát truy cập
monitor.start_monitoring()
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../../../LICENSE) để biết thêm chi tiết. 