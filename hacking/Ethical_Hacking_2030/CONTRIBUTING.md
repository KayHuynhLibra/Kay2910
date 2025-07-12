# Hướng dẫn đóng góp

## Quy trình đóng góp

### 1. Fork và Clone
1. Fork repository này
2. Clone repository đã fork về máy local:
```bash
git clone https://github.com/your-username/Ethical_Hacking_2030.git
```

### 2. Tạo Branch
Tạo một branch mới cho mỗi tính năng hoặc sửa lỗi:
```bash
git checkout -b feature/your-feature-name
# hoặc
git checkout -b fix/your-fix-name
```

### 3. Phát triển
1. Tuân thủ coding style và conventions
2. Thêm comments và documentation khi cần thiết
3. Viết unit tests cho code mới
4. Đảm bảo tất cả tests đều pass

### 4. Commit
1. Commit message phải rõ ràng và mô tả được thay đổi
2. Sử dụng các prefix phù hợp:
   - `feat:` cho tính năng mới
   - `fix:` cho sửa lỗi
   - `docs:` cho thay đổi documentation
   - `style:` cho thay đổi format
   - `refactor:` cho refactor code
   - `test:` cho thêm/sửa tests
   - `chore:` cho thay đổi build process

### 5. Push và Pull Request
1. Push branch lên repository của bạn:
```bash
git push origin feature/your-feature-name
```
2. Tạo Pull Request từ branch của bạn vào main branch
3. Mô tả chi tiết các thay đổi trong PR
4. Đợi review và phản hồi các comments

## Coding Standards

### Python
- Tuân thủ PEP 8
- Sử dụng type hints
- Viết docstrings cho tất cả functions và classes
- Đặt tên biến và hàm có ý nghĩa
- Tối đa độ dài dòng là 88 ký tự

### Documentation
- Sử dụng Markdown cho tất cả documentation
- Cập nhật README.md khi thêm tính năng mới
- Thêm comments cho code phức tạp
- Cập nhật API documentation

### Testing
- Viết unit tests cho tất cả code mới
- Đảm bảo test coverage > 80%
- Sử dụng pytest cho testing
- Thêm integration tests khi cần thiết

## Quy trình Review

### Pull Request Review
1. Code review sẽ được thực hiện bởi ít nhất 1 maintainer
2. Tất cả tests phải pass
3. Code phải tuân thủ coding standards
4. Documentation phải được cập nhật
5. Không có conflicts với main branch

### Feedback
1. Maintainers sẽ review và đưa ra feedback
2. Contributors cần phản hồi và sửa đổi theo feedback
3. PR sẽ được merge khi đạt yêu cầu

## Báo cáo lỗi

### Issue Template
Khi báo cáo lỗi, vui lòng sử dụng template sau:
```
## Mô tả lỗi
[Chi tiết về lỗi]

## Các bước tái hiện
1. [Bước 1]
2. [Bước 2]
...

## Kết quả mong đợi
[Mô tả kết quả mong đợi]

## Screenshots
[Nếu có]

## Môi trường
- OS: [e.g. Windows 10]
- Python version: [e.g. 3.8.0]
- Các dependencies: [e.g. numpy==1.19.0]

## Thông tin thêm
[Thông tin bổ sung nếu có]
```

## Liên hệ
Nếu bạn có bất kỳ câu hỏi nào, vui lòng:
1. Tạo issue với label "question"
2. Liên hệ qua email: your.email@example.com
3. Tham gia Discord channel: [link] 