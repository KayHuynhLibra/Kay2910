# AIDEV Learning Dashboard

## 🎯 Tổng quan

AIDEV Learning Dashboard là một giao diện học tập trực quan để khám phá và học code từ dự án AIDEV. Giao diện này cung cấp:

- **Navigation đơn giản** từ trang chủ đến các bài học chi tiết
- **Liên kết trực tiếp** với các file code thực tế trong dự án
- **Code viewer** với syntax highlighting
- **Thông tin thư mục** cho các learning paths

## 🚀 Cách sử dụng

### 1. Khởi động server

```bash
# Di chuyển vào thư mục learning_dashboard
cd learning_dashboard

# Khởi động Python HTTP server
python -m http.server 8000
```

### 2. Truy cập giao diện

Mở trình duyệt và truy cập:
- **Giao diện chính**: `http://localhost:8000/index.html`
- **Giao diện đơn giản**: `http://localhost:8000/simple-learning.html`

## 📚 Các Learning Paths

### 1. Python Cơ Bản
**Thư mục**: `learning/01_basic_programming/python_basics/`

- **01_variables.py** - Biến và kiểu dữ liệu
- **02_control_structures.py** - Cấu trúc điều khiển
- **03_functions.py** - Hàm và module
- **04_file_handling.py** - Xử lý file

### 2. Python OOP
**Thư mục**: `learning/python_basics/02_oop/`

- **classes.py** - Classes và objects
- **inheritance.py** - Inheritance và polymorphism
- **encapsulation.py** - Encapsulation và access modifiers

### 3. Web Development
**Thư mục**: `learning/02_web_development/`

- **REST API** - `backend/01_rest_api/`
- **GraphQL** - `backend/02_graphql/`
- **WebSockets** - `backend/03_websockets/`
- **Microservices** - `backend/04_microservices/`

### 4. Data Science
**Thư mục**: `learning/04_data_science/`

- **Data Analysis** - `data_analysis/`
- **Statistics** - `statistics/`
- **Data Visualization** - `visualization/`
- **Machine Learning** - `learning/05_machine_learning/`

### 5. AI Agents
**Thư mục**: `ai_system/agents/`

- **Base Agent** - `base_agent.py`
- **Learning Agent** - `learning_agent.py`
- **Chat Agent** - `chat_agent.py`
- **Task Agent** - `task_agent.py`

## 🎨 Tính năng

### Code Viewer
- Hiển thị code với syntax highlighting
- Hiển thị đường dẫn file thực tế
- Copy code functionality

### Directory Info
- Thông tin thư mục cho các learning paths
- Nút mở thư mục trực tiếp
- Hướng dẫn sử dụng

### Navigation
- Chuyển đổi giữa các learning paths
- Nút quay lại trang chủ
- Responsive design

## 🔧 Cấu trúc file

```
learning_dashboard/
├── index.html              # Giao diện chính (đầy đủ tính năng)
├── simple-learning.html    # Giao diện đơn giản (liên kết file thực tế)
├── app.js                  # JavaScript cho giao diện chính
├── styles.css              # CSS styles
└── README.md               # Hướng dẫn sử dụng
```

## 📖 Hướng dẫn học tập

### Bước 1: Chọn Learning Path
Từ trang chủ, click vào learning path bạn muốn học:
- Python Cơ Bản
- Python OOP
- Web Development
- Data Science
- AI Agents

### Bước 2: Chọn bài học
Trong learning path, click vào bài học cụ thể để:
- Xem code thực tế (nếu có file Python)
- Xem thông tin thư mục (cho các learning paths khác)

### Bước 3: Học và thực hành
- Đọc code với syntax highlighting
- Copy code để thực hành
- Mở thư mục để xem các file liên quan

## 🛠️ Troubleshooting

### Lỗi "File không tìm thấy"
- Kiểm tra đường dẫn file có chính xác không
- Đảm bảo server đang chạy từ thư mục đúng
- Kiểm tra file có tồn tại trong dự án không

### Lỗi "Không thể tải file"
- Kiểm tra kết nối internet
- Đảm bảo file không bị khóa
- Thử refresh trang

### Lỗi PowerShell với `&&`
Trong PowerShell, sử dụng:
```powershell
cd learning_dashboard
python -m http.server 8000
```

Thay vì:
```bash
cd learning_dashboard && python -m http.server 8000
```

## 🎯 Mục tiêu học tập

### Python Cơ Bản
- Hiểu biến và kiểu dữ liệu
- Nắm vững cấu trúc điều khiển
- Thành thạo hàm và module
- Biết xử lý file

### Python OOP
- Hiểu classes và objects
- Nắm vững inheritance
- Thành thạo encapsulation
- Áp dụng polymorphism

### Web Development
- Hiểu REST API
- Nắm vững GraphQL
- Thành thạo WebSockets
- Biết microservices

### Data Science
- Hiểu phân tích dữ liệu
- Nắm vững thống kê
- Thành thạo visualization
- Biết machine learning

### AI Agents
- Hiểu agent architecture
- Nắm vững learning agents
- Thành thạo chat agents
- Biết task agents

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy:
1. Kiểm tra README này
2. Xem console trong browser (F12)
3. Kiểm tra terminal output
4. Đảm bảo file paths chính xác

## 🚀 Phát triển tiếp theo

Các tính năng có thể phát triển thêm:
- Progress tracking
- Quiz và exercises
- Code execution
- Collaborative learning
- Mobile app

---

**AIDEV Learning Dashboard** - Học code thực tế từ dự án AIDEV! 🎓 