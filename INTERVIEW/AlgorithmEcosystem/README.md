# 🚀 Algorithm Ecosystem - Hệ sinh thái thuật toán

Một nền tảng học tập thuật toán toàn diện với giao diện hiện đại, nội dung chi tiết và trải nghiệm người dùng tối ưu.

## 📋 Tổng quan

Algorithm Ecosystem là một hệ thống học tập thuật toán trực tuyến được thiết kế để giúp người học từ cơ bản đến nâng cao. Hệ thống bao gồm:

- **8 thuật toán cốt lõi** với nội dung chi tiết
- **3 danh mục chính**: Cơ bản, Sắp xếp, Đồ thị
- **Giao diện thân thiện** với responsive design
- **Hướng dẫn từng bước** cho mỗi thuật toán
- **Code mẫu** và phân tích độ phức tạp
- **Hệ thống PWA** để sử dụng offline

## 🎯 Các thuật toán đã phát triển

### 🔰 Cơ bản
1. **Two Sum** - Tìm hai số có tổng bằng target
2. **Binary Search** - Tìm kiếm nhị phân

### 📊 Sắp xếp
3. **Bubble Sort** - Sắp xếp nổi bọt
4. **Quick Sort** - Sắp xếp nhanh (chia để trị)
5. **Merge Sort** - Sắp xếp trộn

### 🕸️ Đồ thị
6. **Depth First Search (DFS)** - Tìm kiếm theo chiều sâu
7. **Breadth First Search (BFS)** - Tìm kiếm theo chiều rộng
8. **Dijkstra's Algorithm** - Tìm đường đi ngắn nhất

## 🏗️ Cấu trúc dự án

```
AlgorithmEcosystem/
├── ui/                          # Giao diện người dùng
│   ├── index.html              # Trang chủ
│   ├── simple_learning.html    # Học đơn giản
│   ├── algorithm_learning.html # Học chi tiết
│   ├── algorithm_overview.html # Tổng quan thuật toán
│   ├── shared/                 # Tài nguyên chung
│   │   ├── styles.css         # CSS chính
│   │   ├── animations.css     # Hiệu ứng
│   │   ├── utilities.css      # Tiện ích
│   │   ├── animations.js      # JavaScript
│   │   └── service-worker.js  # Service Worker
│   ├── analyzers/             # Phân tích thuật toán
│   ├── components/            # Thành phần UI
│   ├── dashboards/            # Bảng điều khiển
│   ├── learning/              # Học tập
│   └── viewers/               # Trình xem
├── docs/                      # Tài liệu
├── icons/                     # Biểu tượng PWA
└── README.md                  # Tài liệu này
```

## 🚀 Cách sử dụng

### 1. Khởi chạy máy chủ local
```bash
# Sử dụng Python
python -m http.server 8000

# Hoặc sử dụng Node.js
npx serve AlgorithmEcosystem/ui
```

### 2. Truy cập ứng dụng
Mở trình duyệt và truy cập:
- **Trang chủ**: http://localhost:8000/
- **Học đơn giản**: http://localhost:8000/simple_learning.html
- **Học chi tiết**: http://localhost:8000/algorithm_learning.html
- **Tổng quan**: http://localhost:8000/algorithm_overview.html

### 3. Tính năng chính

#### 📖 Học đơn giản
- Giao diện thân thiện cho người mới bắt đầu
- Phân loại theo mức độ khó
- Truy cập nhanh đến các thuật toán phổ biến

#### 🎓 Học chi tiết
- Sidebar với danh sách thuật toán có phân loại
- Tìm kiếm thuật toán
- Nội dung từng bước chi tiết:
  - Mô tả vấn đề
  - Ý tưởng giải thuật
  - Code mẫu
  - Phân tích độ phức tạp
  - Bài tập luyện tập

#### 📊 Tổng quan
- Thống kê tiến độ phát triển
- Danh sách tất cả thuật toán
- Trạng thái hoàn thành
- Điều hướng nhanh

## 🎨 Tính năng giao diện

### Responsive Design
- Tương thích với mọi thiết bị
- Layout thích ứng tự động
- Touch-friendly trên mobile

### Animations & Effects
- Hiệu ứng hover và transition
- Loading animations
- Progress bars động

### Accessibility
- Semantic HTML
- ARIA labels
- Keyboard navigation
- High contrast support

### PWA Features
- Service Worker cho offline access
- App manifest
- Install prompt
- Background sync

## 🔧 Tùy chỉnh và phát triển

### Thêm thuật toán mới
1. Tạo nội dung trong `algorithm_learning.html`
2. Thêm vào sidebar với category phù hợp
3. Cập nhật `algorithm_overview.html`
4. Kiểm tra responsive design

### Tùy chỉnh giao diện
- CSS variables trong `shared/styles.css`
- Animation settings trong `shared/animations.css`
- Utility classes trong `shared/utilities.css`

### Tối ưu hóa
```bash
# Chạy script tối ưu hóa
python optimize_all_html.py
```

## 📈 Tiến độ phát triển

- ✅ **80% hoàn thành** - 8/10 thuật toán cốt lõi
- ✅ Giao diện người dùng hoàn chỉnh
- ✅ Hệ thống PWA
- ✅ Responsive design
- 🚧 Thuật toán nâng cao (Dynamic Programming, Greedy, Backtracking)

## 🛠️ Công nghệ sử dụng

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Animations**: CSS Transitions, JavaScript
- **PWA**: Service Workers, Web App Manifest
- **Development**: Python scripts for automation

## 🤝 Đóng góp

Để đóng góp vào dự án:

1. Fork repository
2. Tạo feature branch
3. Thêm thuật toán mới hoặc cải thiện giao diện
4. Kiểm tra responsive design
5. Submit pull request

## 📝 License

Dự án này được phát hành dưới MIT License.

## 📞 Liên hệ

- **Email**: algorithm.ecosystem@example.com
- **GitHub**: [Algorithm Ecosystem Repository]
- **Website**: [Algorithm Ecosystem Platform]

---

**Made with ❤️ for the programming community** 