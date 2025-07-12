# Model Stealing Module

## Overview
Module chống trộm mô hình cung cấp các công cụ và kỹ thuật để bảo vệ mô hình AI khỏi việc bị sao chép trái phép.

## Các Kỹ Thuật

### 1. Model Extraction Detection
- **Mô tả**: Phát hiện các nỗ lực trích xuất mô hình
- **Công dụng**: Phát hiện tấn công trộm mô hình
- **Tham số**:
  - threshold: Ngưỡng phát hiện
  - window_size: Kích thước cửa sổ
  - detection_rate: Tỷ lệ phát hiện

### 2. Watermarking
- **Mô tả**: Nhúng watermark vào mô hình
- **Công dụng**: Xác thực quyền sở hữu
- **Tham số**:
  - watermark_type: Loại watermark
  - strength: Độ mạnh
  - position: Vị trí nhúng

### 3. Model Fingerprinting
- **Mô tả**: Tạo dấu vân tay cho mô hình
- **Công dụng**: Xác định nguồn gốc mô hình
- **Tham số**:
  - fingerprint_type: Loại dấu vân tay
  - length: Độ dài
  - uniqueness: Độ độc nhất

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.ai_security.model_stealing import ModelProtection

# Khởi tạo bảo vệ
protection = ModelProtection(model)

# Thêm watermark
watermarked_model = protection.add_watermark()

# Kiểm tra watermark
is_valid = protection.verify_watermark(watermarked_model)
```

## Ví dụ

### 1. Thêm Watermark
```python
from ethical_hacking_2030.ai_security.model_stealing import Watermarking

# Khởi tạo watermarking
watermarker = Watermarking(
    model=model,
    watermark_type="invisible",
    strength=0.1
)

# Thêm watermark
watermarked_model = watermarker.add_watermark()

# Lưu mô hình
watermarked_model.save("watermarked_model.h5")
```

### 2. Tạo Fingerprint
```python
from ethical_hacking_2030.ai_security.model_stealing import Fingerprinting

# Khởi tạo fingerprinting
fingerprinter = Fingerprinting(
    model=model,
    fingerprint_type="neural",
    length=128
)

# Tạo fingerprint
fingerprint = fingerprinter.generate()

# Lưu fingerprint
fingerprinter.save("model_fingerprint.pkl")
```

## Phòng chống

### 1. Model Obfuscation
```python
from ethical_hacking_2030.ai_security.model_stealing import ModelObfuscation

# Khởi tạo obfuscation
obfuscator = ModelObfuscation(
    model=model,
    obfuscation_type="neural",
    strength=0.5
)

# Làm rối mô hình
obfuscated_model = obfuscator.obfuscate()
```

### 2. Access Control
```python
from ethical_hacking_2030.ai_security.model_stealing import AccessControl

# Khởi tạo access control
controller = AccessControl(
    model=model,
    auth_type="api_key",
    rate_limit=100
)

# Kiểm tra quyền truy cập
is_allowed = controller.check_access(api_key)
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../../../LICENSE) để biết thêm chi tiết. 