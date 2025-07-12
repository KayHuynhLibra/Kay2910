# 🌐 AI/ML Learning Dashboard

## 🎯 Mục đích
- Giao diện web trực quan để học tập, truy cập nhanh tài liệu AI/ML
- Có thể mở rộng thành dashboard quản lý học tập cá nhân
- Responsive, dễ dùng trên cả máy tính và điện thoại

## 📁 Cấu trúc thư mục
```
21_Dashboard_Web/
├── index.html         # Trang chính dashboard
├── style.css          # Giao diện CSS
├── app.js             # Logic JS (load sub HTML)
├── overview.html      # Nội dung Tổng quan
├── theory.html        # Nội dung Lý thuyết
├── quiz.html          # Nội dung Quiz
├── code.html          # Nội dung Code Examples
├── project.html       # Nội dung Project
├── datasets.html      # Bộ dữ liệu mẫu
├── roadmap.html       # Lộ trình học tập
├── exercises.html     # Bài tập thực hành
├── resources.html     # Tài liệu tham khảo
├── assets/            # Ảnh/logo, tài nguyên tĩnh
└── README.md          # Hướng dẫn sử dụng
```

## 🚀 Cách sử dụng
1. Mở file `index.html` bằng trình duyệt (Chrome, Edge, Firefox...)
2. Click các mục ở sidebar để xem nội dung (mỗi mục sẽ load file HTML riêng)
3. Có thể chỉnh sửa từng file HTML nhỏ để cập nhật nội dung mà không cần sửa code JS

## 🛠️ Mở rộng dashboard
- **Thêm mục mới:**
  1. Tạo file mới, ví dụ `mytopic.html`
  2. Thêm mục vào sidebar trong `index.html`:
     ```html
     <li><a href="#" onclick="loadContent('mytopic')">My Topic</a></li>
     ```
  3. Thêm vào `fileMap` trong `app.js`:
     ```js
     mytopic: 'mytopic.html',
     ```
- **Chỉnh sửa giao diện:** Sửa file `style.css`
- **Thêm hình ảnh:** Đặt vào thư mục `assets/`

## 💡 Gợi ý
- Có thể nhúng các file markdown, PDF, hoặc nhúng notebook vào dashboard
- Có thể dùng dashboard này làm nền tảng cho hệ thống học tập cá nhân hoặc nhóm

---
**Chúc bạn học tập hiệu quả với dashboard AI/ML!** 