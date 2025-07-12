# 🚀 AI/ML Learning Dashboard - Hướng Dẫn Sử Dụng

## 📋 Tổng Quan
Dashboard học tập AI/ML với giao diện web hiện đại, cho phép xem nội dung thực tế từ hệ thống 20 chủ đề AI/ML.

## 🎯 Cách Mở Dashboard

### 1. **Windows - Command Line**
```bash
# Cách 1: Sử dụng batch file
open_dashboard.bat

# Cách 2: Sử dụng PowerShell (nhiều tùy chọn)
.\open_dashboard.ps1

# Cách 3: Lệnh trực tiếp
start 21_Dashboard_Web\index.html
```

### 2. **Linux/Mac - Terminal**
```bash
# Cách 1: Sử dụng shell script
chmod +x open_dashboard.sh
./open_dashboard.sh

# Cách 2: Lệnh trực tiếp
xdg-open 21_Dashboard_Web/index.html  # Linux
open 21_Dashboard_Web/index.html      # macOS
```

### 3. **Mở Thủ Công**
- Mở file: `21_Dashboard_Web/index.html` trong trình duyệt
- Hoặc double-click vào file `index.html`

## 🎨 Tính Năng Dashboard

### 📊 **Tổng Quan**
- Thống kê hệ thống: 20 chủ đề, 869 thư mục, 3,785+ bài toán
- Quick actions để truy cập nhanh

### 📚 **Chủ Đề**
- Grid hiển thị 20 chủ đề AI/ML chính
- Link trực tiếp đến từng thư mục chủ đề

### 📁 **Duyệt Files**
- Thống kê chi tiết hệ thống
- Quick links đến các file quan trọng
- Phân loại file types

### 📄 **Xem Nội Dung Thực**
- **Tính năng chính**: Load và hiển thị nội dung từ file markdown thực tế
- Chuyển đổi markdown thành HTML đẹp mắt
- Các loại nội dung:
  - 📖 Lý thuyết (`THEORY_*.md`)
  - 🧠 Quiz (`QUIZ_*.md`)
  - ❓ Bài toán (`COMPLEX_PROBLEMS.md`)
  - 💻 Code (`CODE_EXAMPLES_*.md`)
  - 🚀 Project (`PROJECT_*.md`)

### 🎨 **Giao Diện**
- Responsive design cho mobile/desktop
- Dark/Light theme toggle
- Sidebar với icons và animations
- Card-based layout

## 🔧 Cấu Trúc Files

```
21_Dashboard_Web/
├── index.html          # Trang chính dashboard
├── style.css           # CSS styles
├── script.js           # JavaScript chính
├── load-content.js     # Load nội dung thực tế
├── overview.html       # Trang tổng quan
├── topics.html         # Trang chủ đề
├── browse.html         # Trang duyệt files
├── theory.html         # Trang lý thuyết
├── quiz.html           # Trang quiz
├── code.html           # Trang code examples
├── project.html        # Trang project
├── datasets.html       # Trang datasets
├── roadmap.html        # Trang roadmap
├── exercises.html      # Trang exercises
└── resources.html      # Trang resources
```

## 🚀 Scripts Mở Dashboard

### **open_dashboard.bat** (Windows)
- Mở dashboard trong trình duyệt mặc định
- Kiểm tra file tồn tại
- Hiển thị thông tin hữu ích

### **open_dashboard.ps1** (PowerShell)
- Menu tùy chọn trình duyệt (Chrome, Firefox, Edge)
- Màu sắc và giao diện đẹp
- Xử lý lỗi thông minh

### **open_dashboard.sh** (Linux/Mac)
- Tự động detect hệ điều hành
- Mở trong trình duyệt phù hợp
- Hỗ trợ xdg-open và open

## 💡 Mẹo Sử Dụng

### 1. **Xem Nội Dung Thực**
1. Mở dashboard
2. Click "Xem Nội Dung Thực" trong sidebar
3. Chọn loại nội dung muốn xem
4. Nội dung sẽ được load từ file thực tế

### 2. **Dark Theme**
- Click nút 🌙/☀️ ở header để chuyển đổi theme

### 3. **Mobile Friendly**
- Dashboard responsive, hoạt động tốt trên mobile
- Sidebar có thể ẩn/hiện trên mobile

### 4. **Quick Navigation**
- Sử dụng "Chủ Đề" để xem 20 chủ đề chính
- Sử dụng "Duyệt Files" để xem cấu trúc hệ thống

## 🔗 Liên Kết Nhanh

### **Từ Dashboard:**
- **Chủ Đề** → Xem 20 chủ đề AI/ML
- **Duyệt Files** → Xem cấu trúc hệ thống
- **Xem Nội Dung Thực** → Load file markdown thực tế

### **Từ File System:**
- `01_Machine_Learning/` → Machine Learning
- `02_Deep_Learning/` → Deep Learning
- `03_Neural_Networks/` → Neural Networks
- `04_Natural_Language_Processing/` → NLP
- `05_Computer_Vision/` → Computer Vision
- ... và 15 chủ đề khác

## 🛠️ Troubleshooting

### **Dashboard không mở:**
1. Kiểm tra file `21_Dashboard_Web/index.html` tồn tại
2. Đảm bảo đang ở thư mục gốc của dự án
3. Thử mở thủ công trong trình duyệt

### **Nội dung không load:**
1. Kiểm tra file markdown tồn tại
2. Đảm bảo đường dẫn file đúng
3. Kiểm tra console browser để xem lỗi

### **Giao diện lỗi:**
1. Refresh trang (F5)
2. Clear cache browser
3. Kiểm tra file CSS/JS tồn tại

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra README này
2. Xem console browser (F12)
3. Đảm bảo tất cả files tồn tại
4. Thử mở thủ công file `index.html`

---

**🎉 Chúc bạn học tập hiệu quả với AI/ML Dashboard!** 