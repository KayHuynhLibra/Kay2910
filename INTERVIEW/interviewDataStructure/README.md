# 14 PHƯƠNG PHÁP PHÂN TÍCH & THIẾT KẾ GIẢI THUẬT ĐỂ VƯỢT QUA VÒNG INTERVIEW GIẢI THUẬT

## Tổng quan
Tài liệu này tổng hợp 14 phương pháp phân tích và thiết kế giải thuật quan trọng nhất để vượt qua các vòng phỏng vấn giải thuật. Mỗi phương pháp đều có ứng dụng cụ thể và các bài toán điển hình.

## Danh sách các phương pháp

### 1. Sliding Window (Cửa sổ trượt)
- **Mô tả**: Dùng để thực hiện các thao tác trên một khoảng cố định của mảng hoặc danh sách liên kết
- **Ứng dụng**: Tìm dãy con dài nhất thỏa mãn điều kiện
- **Đặc điểm**: Kích thước cửa sổ có thể thay đổi tùy bài toán

### 2. Two Pointers (Hai con trỏ)
- **Mô tả**: Phù hợp khi so sánh các phần tử trong mảng hoặc danh sách đã sắp xếp
- **Ứng dụng**: Hai con trỏ cùng duyệt dữ liệu, giảm độ phức tạp thời gian
- **Ưu điểm**: Hiệu quả hơn so với việc sử dụng một con trỏ

### 3. Fast and Slow Pointers (Con trỏ nhanh và chậm)
- **Mô tả**: Thường dùng với danh sách liên kết hoặc cấu trúc vòng lặp
- **Ứng dụng**: Phát hiện chu kỳ trong danh sách liên kết
- **Cơ chế**: Con trỏ nhanh và chậm sẽ gặp nhau nếu tồn tại chu kỳ

### 4. Merge Intervals (Gộp khoảng)
- **Mô tả**: Giải quyết các bài toán liên quan đến khoảng chồng lấn
- **Yêu cầu**: Hiểu rõ 6 trường hợp chồng lấn giữa hai khoảng
- **Mục đích**: Xử lý hợp nhất hoặc chèn khoảng

### 5. Cyclic Sort (Sắp xếp vòng lặp)
- **Mô tả**: Dùng cho các mảng chứa số trong một phạm vi xác định
- **Cơ chế**: Duyệt từng phần tử và đặt chúng về đúng vị trí
- **Độ phức tạp**: O(n)

### 6. In-Place Reversal of Linked List (Đảo ngược danh sách liên kết tại chỗ)
- **Mô tả**: Đảo ngược danh sách mà không cần sử dụng bộ nhớ bổ sung
- **Phương pháp**: Sử dụng hai biến con trỏ (current và previous)
- **Ưu điểm**: Tiết kiệm bộ nhớ

### 7. Tree BFS (Duyệt cây theo chiều rộng)
- **Mô tả**: Duyệt cây theo từng tầng bằng cách sử dụng hàng đợi
- **Ứng dụng**: Thích hợp cho các bài toán yêu cầu truy cập cây theo mức
- **Cấu trúc dữ liệu**: Queue

### 8. Tree DFS (Duyệt cây theo chiều sâu)
- **Mô tả**: Duyệt cây theo thứ tự tiền tố, trung tố, hoặc hậu tố
- **Phương pháp**: Sử dụng đệ quy hoặc stack để lưu trữ các nút đã duyệt
- **Ứng dụng**: Tìm kiếm đường đi, tính toán giá trị

### 9. Two Heaps (Hai heap)
- **Mô tả**: Phân chia dữ liệu thành hai phần: Min Heap cho phần lớn nhất và Max Heap cho phần nhỏ nhất
- **Ứng dụng**: Tìm median hoặc top-k phần tử
- **Cấu trúc**: Min Heap + Max Heap

### 10. Subsets (Tập con)
- **Mô tả**: Tạo tập con từ một tập hợp cho trước bằng cách áp dụng BFS
- **Phương pháp**: Bắt đầu từ tập rỗng và thêm lần lượt từng phần tử
- **Kết quả**: Tạo tập con mới

### 11. Modified Binary Search (Tìm kiếm nhị phân mở rộng)
- **Mô tả**: Dùng khi làm việc với dữ liệu đã sắp xếp
- **Lưu ý**: Tránh lỗi tràn số nguyên với công thức `middle = start + (end - start) / 2`
- **Ứng dụng**: Tìm kiếm trong mảng đã sắp xếp

### 12. Top K Elements (K phần tử lớn nhất/nhỏ nhất)
- **Mô tả**: Sử dụng heap để tìm các phần tử lớn nhất, nhỏ nhất, hoặc xuất hiện thường xuyên nhất
- **Cơ chế**: Liên tục duy trì heap với các phần tử phù hợp
- **Ứng dụng**: Phân tích dữ liệu, ranking

### 13. K-Way Merge (Hợp nhất K dãy)
- **Mô tả**: Xử lý nhiều mảng đã sắp xếp bằng cách sử dụng Min Heap để hợp nhất
- **Phương pháp**: Lần lượt lấy phần tử nhỏ nhất từ heap và thay thế bằng phần tử tiếp theo
- **Ứng dụng**: Merge sort, external sorting

### 14. Topological Sort (Sắp xếp topo)
- **Mô tả**: Sắp xếp các phần tử có mối quan hệ phụ thuộc theo thứ tự tuyến tính
- **Phương pháp**: Dùng danh sách kề và in-degree để xác định và xử lý các nút nguồn
- **Ứng dụng**: Dependency resolution, build systems

## Cách sử dụng
Mỗi phương pháp có thư mục riêng chứa:
- Lý thuyết và giải thích chi tiết
- Ví dụ minh họa
- Bài tập thực hành
- Code mẫu

## Lưu ý quan trọng
- Hiểu rõ từng phương pháp trước khi áp dụng
- Thực hành nhiều bài tập để thành thạo
- Chú ý đến độ phức tạp thời gian và không gian
- Biết cách chọn phương pháp phù hợp cho từng bài toán 