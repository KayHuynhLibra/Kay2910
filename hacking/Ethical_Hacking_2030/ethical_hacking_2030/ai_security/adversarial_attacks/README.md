# Adversarial Attacks Module

## Overview
Module tấn công đối kháng cung cấp các công cụ và kỹ thuật để tạo và phòng chống các cuộc tấn công đối kháng vào mô hình AI.

## Các Kỹ Thuật

### 1. FGSM (Fast Gradient Sign Method)
- **Mô tả**: Kỹ thuật tấn công đối kháng nhanh dựa trên gradient
- **Công dụng**: Tạo adversarial examples với nhiễu nhỏ
- **Tham số**:
  - epsilon: Độ lớn của nhiễu
  - clip_min: Giá trị nhỏ nhất
  - clip_max: Giá trị lớn nhất

### 2. PGD (Projected Gradient Descent)
- **Mô tả**: Kỹ thuật tấn công đối kháng lặp
- **Công dụng**: Tạo adversarial examples mạnh
- **Tham số**:
  - steps: Số bước lặp
  - step_size: Kích thước bước
  - epsilon: Giới hạn nhiễu

### 3. DeepFool
- **Mô tả**: Kỹ thuật tìm đường biên gần nhất
- **Công dụng**: Tạo adversarial examples với nhiễu tối thiểu
- **Tham số**:
  - max_iter: Số lần lặp tối đa
  - overshoot: Hệ số vượt quá

### 4. Carlini & Wagner Attack
- **Mô tả**: Kỹ thuật tấn công đối kháng mạnh
- **Công dụng**: Tạo adversarial examples khó phát hiện
- **Tham số**:
  - confidence: Độ tin cậy
  - learning_rate: Tốc độ học
  - binary_search_steps: Số bước tìm kiếm nhị phân

## Cài đặt và Sử dụng

### Yêu cầu
```bash
pip install -r requirements.txt
```

### Sử dụng cơ bản
```python
from ethical_hacking_2030.ai_security.adversarial_attacks import FGSMAttack

# Khởi tạo tấn công
attack = FGSMAttack(model, epsilon=0.03)

# Tạo adversarial example
adversarial_x = attack.generate(x)

# Đánh giá kết quả
result = model.evaluate(adversarial_x)
```

## Ví dụ

### 1. Tấn công FGSM
```python
from ethical_hacking_2030.ai_security.adversarial_attacks import FGSMAttack

# Khởi tạo tấn công
attack = FGSMAttack(
    model=model,
    epsilon=0.03,
    clip_min=0.0,
    clip_max=1.0
)

# Tạo adversarial example
adversarial_x = attack.generate(x)

# Đánh giá kết quả
result = model.evaluate(adversarial_x)
print(f"Accuracy: {result['accuracy']}")
```

### 2. Tấn công PGD
```python
from ethical_hacking_2030.ai_security.adversarial_attacks import PGDAttack

# Khởi tạo tấn công
attack = PGDAttack(
    model=model,
    steps=10,
    step_size=0.01,
    epsilon=0.03
)

# Tạo adversarial example
adversarial_x = attack.generate(x)

# Đánh giá kết quả
result = model.evaluate(adversarial_x)
print(f"Accuracy: {result['accuracy']}")
```

## Phòng chống

### 1. Adversarial Training
```python
from ethical_hacking_2030.ai_security.adversarial_attacks import AdversarialTraining

# Khởi tạo training
trainer = AdversarialTraining(
    model=model,
    attack=FGSMAttack,
    epsilon=0.03
)

# Huấn luyện mô hình
trainer.train(x_train, y_train, epochs=10)
```

### 2. Input Preprocessing
```python
from ethical_hacking_2030.ai_security.adversarial_attacks import InputPreprocessing

# Khởi tạo preprocessing
preprocessor = InputPreprocessing(
    smoothing=True,
    quantization=True
)

# Xử lý input
processed_x = preprocessor.process(x)
```

## Đóng góp
Vui lòng đọc [CONTRIBUTING.md](../../../../CONTRIBUTING.md) để biết thêm chi tiết về quy trình đóng góp.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](../../../../LICENSE) để biết thêm chi tiết. 