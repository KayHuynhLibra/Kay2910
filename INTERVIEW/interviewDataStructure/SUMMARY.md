# TỔNG HỢP 14 PHƯƠNG PHÁP PHÂN TÍCH & THIẾT KẾ GIẢI THUẬT

## 📋 Danh sách đầy đủ các phương pháp

### 1. **Sliding Window (Cửa sổ trượt)**
- **Mục đích**: Thực hiện thao tác trên khoảng cố định của mảng/danh sách
- **Độ phức tạp**: O(n) thời gian, O(1) không gian
- **Ứng dụng**: Tìm dãy con dài nhất, xử lý chuỗi
- **Đặc điểm**: Kích thước cửa sổ có thể cố định hoặc thay đổi

### 2. **Two Pointers (Hai con trỏ)**
- **Mục đích**: So sánh phần tử trong mảng/danh sách đã sắp xếp
- **Độ phức tạp**: O(n) thời gian, O(1) không gian
- **Ứng dụng**: Tìm cặp số, loại bỏ trùng lặp
- **Đặc điểm**: Giảm độ phức tạp so với một con trỏ

### 3. **Fast and Slow Pointers (Con trỏ nhanh và chậm)**
- **Mục đích**: Phát hiện chu kỳ trong danh sách liên kết
- **Độ phức tạp**: O(n) thời gian, O(1) không gian
- **Ứng dụng**: Tìm điểm giữa, phát hiện chu kỳ
- **Đặc điểm**: Con trỏ nhanh di chuyển gấp đôi con trỏ chậm

### 4. **Merge Intervals (Gộp khoảng)**
- **Mục đích**: Xử lý khoảng chồng lấn
- **Độ phức tạp**: O(n log n) thời gian, O(n) không gian
- **Ứng dụng**: Lịch trình, quản lý thời gian
- **Đặc điểm**: Hiểu rõ 6 trường hợp chồng lấn

### 5. **Cyclic Sort (Sắp xếp vòng lặp)**
- **Mục đích**: Sắp xếp mảng chứa số trong phạm vi xác định
- **Độ phức tạp**: O(n) thời gian, O(1) không gian
- **Ứng dụng**: Tìm số thiếu, số trùng lặp
- **Đặc điểm**: Đặt phần tử về đúng vị trí

### 6. **In-Place Reversal of Linked List (Đảo ngược tại chỗ)**
- **Mục đích**: Đảo ngược danh sách không dùng bộ nhớ bổ sung
- **Độ phức tạp**: O(n) thời gian, O(1) không gian
- **Ứng dụng**: Palindrome, reorder list
- **Đặc điểm**: Sử dụng hai biến con trỏ

### 7. **Tree BFS (Duyệt cây theo chiều rộng)**
- **Mục đích**: Duyệt cây theo từng tầng
- **Độ phức tạp**: O(n) thời gian, O(w) không gian (w = chiều rộng)
- **Ứng dụng**: Tìm đường đi ngắn nhất, level order traversal
- **Đặc điểm**: Sử dụng queue

### 8. **Tree DFS (Duyệt cây theo chiều sâu)**
- **Mục đích**: Duyệt cây theo thứ tự tiền tố, trung tố, hậu tố
- **Độ phức tạp**: O(n) thời gian, O(h) không gian (h = chiều cao)
- **Ứng dụng**: Tìm kiếm đường đi, tính toán giá trị
- **Đặc điểm**: Sử dụng đệ quy hoặc stack

### 9. **Two Heaps (Hai heap)**
- **Mục đích**: Phân chia dữ liệu thành hai phần
- **Độ phức tạp**: O(log n) thời gian cho mỗi thao tác
- **Ứng dụng**: Tìm median, top-k phần tử
- **Đặc điểm**: Min Heap + Max Heap

### 10. **Subsets (Tập con)**
- **Mục đích**: Tạo tập con từ tập hợp cho trước
- **Độ phức tạp**: O(2^n) thời gian, O(2^n) không gian
- **Ứng dụng**: Backtracking, combination
- **Đặc điểm**: Sử dụng BFS hoặc backtracking

### 11. **Modified Binary Search (Tìm kiếm nhị phân mở rộng)**
- **Mục đích**: Tìm kiếm trong dữ liệu đã sắp xếp
- **Độ phức tạp**: O(log n) thời gian, O(1) không gian
- **Ứng dụng**: Tìm kiếm, tìm vị trí chèn
- **Đặc điểm**: Tránh tràn số nguyên

### 12. **Top K Elements (K phần tử lớn nhất/nhỏ nhất)**
- **Mục đích**: Tìm k phần tử theo tiêu chí
- **Độ phức tạp**: O(n log k) thời gian, O(k) không gian
- **Ứng dụng**: Ranking, phân tích dữ liệu
- **Đặc điểm**: Sử dụng heap

### 13. **K-Way Merge (Hợp nhất K dãy)**
- **Mục đích**: Hợp nhất nhiều mảng đã sắp xếp
- **Độ phức tạp**: O(n log k) thời gian, O(k) không gian
- **Ứng dụng**: Merge sort, external sorting
- **Đặc điểm**: Sử dụng Min Heap

### 14. **Topological Sort (Sắp xếp topo)**
- **Mục đích**: Sắp xếp theo thứ tự phụ thuộc
- **Độ phức tạp**: O(V + E) thời gian, O(V) không gian
- **Ứng dụng**: Dependency resolution, build systems
- **Đặc điểm**: Sử dụng DFS hoặc BFS

## 🎯 Chiến lược chọn phương pháp

### Dựa trên loại dữ liệu:
- **Mảng/Chuỗi**: Sliding Window, Two Pointers, Binary Search
- **Danh sách liên kết**: Fast/Slow Pointers, In-Place Reversal
- **Cây**: BFS, DFS
- **Đồ thị**: Topological Sort, BFS, DFS
- **Khoảng thời gian**: Merge Intervals

### Dựa trên yêu cầu bài toán:
- **Tìm kiếm**: Binary Search, Two Pointers
- **Sắp xếp**: Cyclic Sort, Topological Sort
- **Tối ưu hóa**: Sliding Window, Two Heaps
- **Tổ hợp**: Subsets, Backtracking
- **Phân tích**: Top K Elements, K-Way Merge

## 📊 So sánh độ phức tạp

| Phương pháp | Thời gian | Không gian | Ứng dụng chính |
|-------------|-----------|------------|----------------|
| Sliding Window | O(n) | O(1) | Xử lý chuỗi/mảng |
| Two Pointers | O(n) | O(1) | So sánh phần tử |
| Fast/Slow | O(n) | O(1) | Phát hiện chu kỳ |
| Merge Intervals | O(n log n) | O(n) | Khoảng thời gian |
| Cyclic Sort | O(n) | O(1) | Sắp xếp phạm vi |
| In-Place Reversal | O(n) | O(1) | Đảo ngược |
| Tree BFS | O(n) | O(w) | Duyệt theo tầng |
| Tree DFS | O(n) | O(h) | Duyệt theo chiều sâu |
| Two Heaps | O(log n) | O(n) | Median/Top-K |
| Subsets | O(2^n) | O(2^n) | Tổ hợp |
| Binary Search | O(log n) | O(1) | Tìm kiếm |
| Top K | O(n log k) | O(k) | Ranking |
| K-Way Merge | O(n log k) | O(k) | Hợp nhất |
| Topological Sort | O(V+E) | O(V) | Sắp xếp phụ thuộc |

## 💡 Mẹo quan trọng

### 1. **Phân tích bài toán**:
- Xác định loại dữ liệu đầu vào
- Hiểu rõ yêu cầu đầu ra
- Xác định các ràng buộc

### 2. **Chọn phương pháp**:
- Dựa trên đặc điểm dữ liệu
- Xem xét độ phức tạp yêu cầu
- Kết hợp nhiều phương pháp nếu cần

### 3. **Tối ưu hóa**:
- Chú ý đến edge cases
- Xử lý các trường hợp đặc biệt
- Tối ưu hóa bộ nhớ và thời gian

### 4. **Thực hành**:
- Làm nhiều bài tập cho mỗi phương pháp
- Hiểu sâu nguyên lý hoạt động
- Biết cách áp dụng linh hoạt

## 🚀 Lộ trình học tập

### **Giai đoạn 1: Nền tảng**
1. Two Pointers
2. Sliding Window
3. Binary Search

### **Giai đoạn 2: Cấu trúc dữ liệu**
4. Fast/Slow Pointers
5. In-Place Reversal
6. Tree BFS/DFS

### **Giai đoạn 3: Nâng cao**
7. Merge Intervals
8. Cyclic Sort
9. Two Heaps

### **Giai đoạn 4: Chuyên sâu**
10. Subsets
11. Top K Elements
12. K-Way Merge
13. Topological Sort

### **Giai đoạn 5: Tổng hợp**
- Kết hợp nhiều phương pháp
- Giải các bài toán phức tạp
- Tối ưu hóa giải thuật 