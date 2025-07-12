# Cấu Trúc Dự Án AI

```
ai_system/
├── README.md                 # Tài liệu tổng quan về dự án
├── requirements.txt          # Dependencies chính của dự án
├── main.py                   # Entry point của ứng dụng
│
├── agents/                   # Thư mục chứa các agent
│   ├── __init__.py
│   ├── base_agent.py        # Lớp cơ sở cho tất cả các agent
│   ├── chat_agent.py        # Agent xử lý chat
│   ├── learning_agent.py    # Agent học tập
│   └── statistical_agent.py # Agent thống kê
│
├── core/                     # Thư mục chứa các thành phần cốt lõi
│   ├── __init__.py
│   ├── config.py            # Cấu hình hệ thống
│   ├── memory.py            # Quản lý bộ nhớ
│   └── utils.py             # Các tiện ích
│
├── data/                     # Thư mục dữ liệu
│   ├── raw/                 # Dữ liệu thô
│   └── processed/           # Dữ liệu đã xử lý
│
├── models/                   # Thư mục chứa các mô hình
│   ├── __init__.py
│   └── model_manager.py     # Quản lý mô hình
│
├── stats/                    # Module thống kê
│   ├── __init__.py
│   ├── README.md            # Tài liệu module thống kê
│   ├── requirements.txt     # Dependencies cho module thống kê
│   └── statistical_agent.py # Agent thống kê
│
└── tests/                    # Thư mục chứa các test
    ├── __init__.py
    ├── test_agents/         # Test cho các agent
    ├── test_core/           # Test cho core
    └── test_stats/          # Test cho module thống kê
```

## Mô Tả Chi Tiết

### 1. Thư Mục Gốc
- `README.md`: Tài liệu tổng quan về dự án, hướng dẫn cài đặt và sử dụng
- `requirements.txt`: Danh sách các thư viện cần thiết cho dự án
- `main.py`: Điểm khởi đầu của ứng dụng, chứa logic chính

### 2. Thư Mục Agents
Chứa các agent xử lý các nhiệm vụ khác nhau:
- `base_agent.py`: Lớp cơ sở định nghĩa các phương thức chung
- `chat_agent.py`: Xử lý tương tác chat
- `learning_agent.py`: Quản lý quá trình học tập
- `statistical_agent.py`: Xử lý các phân tích thống kê

### 3. Thư Mục Core
Chứa các thành phần cốt lõi của hệ thống:
- `config.py`: Quản lý cấu hình hệ thống
- `memory.py`: Quản lý bộ nhớ và lưu trữ
- `utils.py`: Các hàm tiện ích dùng chung

### 4. Thư Mục Data
Quản lý dữ liệu:
- `raw/`: Chứa dữ liệu thô chưa xử lý
- `processed/`: Chứa dữ liệu đã được xử lý

### 5. Thư Mục Models
Quản lý các mô hình AI:
- `model_manager.py`: Quản lý việc tải, lưu và sử dụng các mô hình

### 6. Module Stats
Module thống kê độc lập:
- `README.md`: Tài liệu chi tiết về module
- `requirements.txt`: Dependencies riêng cho module
- `statistical_agent.py`: Agent xử lý các phân tích thống kê

### 7. Thư Mục Tests
Chứa các test case:
- `test_agents/`: Test cho các agent
- `test_core/`: Test cho các thành phần core
- `test_stats/`: Test cho module thống kê

## Các Tính Năng Chính

1. **Hệ Thống Agent**
   - Chat Agent: Xử lý tương tác người dùng
   - Learning Agent: Quản lý quá trình học tập
   - Statistical Agent: Phân tích thống kê

2. **Quản Lý Dữ Liệu**
   - Lưu trữ dữ liệu thô và đã xử lý
   - Quản lý bộ nhớ và cache

3. **Phân Tích Thống Kê**
   - Thống kê mô tả
   - Phân phối xác suất
   - Kiểm định giả thuyết
   - Phân tích tương quan
   - Phân tích hồi quy

4. **Testing**
   - Unit tests
   - Integration tests
   - Performance tests

## Cài Đặt và Sử Dụng

1. Cài đặt dependencies chính:
```bash
pip install -r requirements.txt
```

2. Cài đặt dependencies cho module thống kê:
```bash
cd stats
pip install -r requirements.txt
```

3. Chạy ứng dụng:
```bash
python main.py
```

## Lưu ý
- Đảm bảo Python 3.8+ được cài đặt
- Tạo môi trường ảo trước khi cài đặt
- Kiểm tra các biến môi trường cần thiết
- Chạy tests trước khi deploy 