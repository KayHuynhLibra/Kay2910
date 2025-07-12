# Web Security Fundamentals / Cơ Bản Bảo Mật Web

## Introduction / Giới Thiệu

### What is Web Security? / Bảo Mật Web là gì?
- Protecting web applications / Bảo vệ ứng dụng web
- Preventing attacks / Ngăn chặn tấn công
- Securing data / Bảo mật dữ liệu
- User protection / Bảo vệ người dùng

### Common Web Technologies / Công Nghệ Web Phổ Biến
```
Frontend / Giao diện người dùng:
- HTML / HTML
- CSS / CSS
- JavaScript / JavaScript
- React / React
- Angular / Angular

Backend / Phía máy chủ:
- PHP / PHP
- Python / Python
- Node.js / Node.js
- Java / Java
- .NET / .NET

Databases / Cơ sở dữ liệu:
- MySQL / MySQL
- PostgreSQL / PostgreSQL
- MongoDB / MongoDB
- Redis / Redis
```

## Web Architecture / Kiến Trúc Web

### Client-Server Model / Mô Hình Client-Server
```
Client / Máy khách:
- Browser / Trình duyệt
- Mobile apps / Ứng dụng di động
- Desktop apps / Ứng dụng máy tính

Server / Máy chủ:
- Web server / Máy chủ web
- Application server / Máy chủ ứng dụng
- Database server / Máy chủ cơ sở dữ liệu
```

### HTTP Protocol / Giao Thức HTTP
```
Methods / Phương thức:
GET - Retrieve data / Lấy dữ liệu
POST - Submit data / Gửi dữ liệu
PUT - Update data / Cập nhật dữ liệu
DELETE - Remove data / Xóa dữ liệu

Headers / Tiêu đề:
- Content-Type / Loại nội dung
- Authorization / Xác thực
- Cookie / Cookie
- Cache-Control / Kiểm soát bộ nhớ đệm
```

## Common Vulnerabilities / Lỗ Hổng Thường Gặp

### OWASP Top 10 / Top 10 OWASP
```
1. Injection / Tiêm mã
2. Broken Authentication / Xác thực bị hỏng
3. Sensitive Data Exposure / Lộ dữ liệu nhạy cảm
4. XML External Entities / Thực thể bên ngoài XML
5. Broken Access Control / Kiểm soát truy cập bị hỏng
6. Security Misconfiguration / Cấu hình bảo mật sai
7. XSS / Tấn công XSS
8. Insecure Deserialization / Giải tuần tự hóa không an toàn
9. Using Components with Known Vulnerabilities / Sử dụng thành phần có lỗ hổng
10. Insufficient Logging & Monitoring / Ghi log và giám sát không đủ
```

### SQL Injection / Tiêm SQL
```
Example / Ví dụ:
' OR '1'='1
UNION SELECT * FROM users
DROP TABLE users

Prevention / Phòng chống:
- Prepared statements / Câu lệnh chuẩn bị
- Input validation / Kiểm tra đầu vào
- Parameterized queries / Truy vấn tham số hóa
```

### Cross-Site Scripting (XSS) / Tấn Công XSS
```
Types / Loại:
- Reflected XSS / XSS phản xạ
- Stored XSS / XSS lưu trữ
- DOM-based XSS / XSS dựa trên DOM

Prevention / Phòng chống:
- Input sanitization / Làm sạch đầu vào
- Output encoding / Mã hóa đầu ra
- Content Security Policy / Chính sách bảo mật nội dung
```

### Cross-Site Request Forgery (CSRF) / Tấn Công CSRF
```
Example / Ví dụ:
<img src="http://bank.com/transfer?amount=1000&to=attacker">

Prevention / Phòng chống:
- CSRF tokens / Token CSRF
- SameSite cookies / Cookie SameSite
- Custom headers / Tiêu đề tùy chỉnh
```

## Security Controls / Kiểm Soát Bảo Mật

### Authentication / Xác Thực
```
Methods / Phương thức:
- Username/password / Tên đăng nhập/mật khẩu
- Multi-factor / Đa yếu tố
- OAuth / OAuth
- SAML / SAML

Best Practices / Thực hành tốt nhất:
- Password hashing / Băm mật khẩu
- Session management / Quản lý phiên
- Account lockout / Khóa tài khoản
- Secure password reset / Đặt lại mật khẩu an toàn
```

### Authorization / Phân Quyền
```
Models / Mô hình:
- Role-based / Dựa trên vai trò
- Attribute-based / Dựa trên thuộc tính
- Policy-based / Dựa trên chính sách

Implementation / Triển khai:
- Access control lists / Danh sách kiểm soát truy cập
- JWT tokens / Token JWT
- OAuth scopes / Phạm vi OAuth
```

### Data Protection / Bảo Vệ Dữ Liệu
```
Encryption / Mã hóa:
- TLS/SSL / TLS/SSL
- Data at rest / Dữ liệu lưu trữ
- Data in transit / Dữ liệu truyền tải

Storage / Lưu trữ:
- Secure cookies / Cookie an toàn
- Local storage / Lưu trữ cục bộ
- Session storage / Lưu trữ phiên
```

## Security Tools / Công Cụ Bảo Mật

### Scanning Tools / Công Cụ Quét
```
OWASP ZAP:
zap-cli quick-scan --self-contained --start-options "-config api.disablekey=true" http://target

Burp Suite:
# Configure browser proxy
# Intercept and analyze traffic
```

### Testing Tools / Công Cụ Kiểm Thử
```
SQLMap:
sqlmap -u "http://target.com/page.php?id=1"

XSSer:
xsser --url "http://target.com" --auto
```

### Monitoring Tools / Công Cụ Giám Sát
```
ModSecurity:
# Web Application Firewall
# Real-time monitoring
# Attack detection

Snort:
# Network intrusion detection
# Traffic analysis
# Alert generation
```

## Secure Development / Phát Triển An Toàn

### Secure Coding / Lập Trình An Toàn
```
Principles / Nguyên tắc:
- Input validation / Kiểm tra đầu vào
- Output encoding / Mã hóa đầu ra
- Error handling / Xử lý lỗi
- Secure defaults / Mặc định an toàn
```

### Code Review / Đánh Giá Mã
```
Checklist / Danh sách kiểm tra:
- Security vulnerabilities / Lỗ hổng bảo mật
- Best practices / Thực hành tốt nhất
- Code quality / Chất lượng mã
- Documentation / Tài liệu
```

### Testing / Kiểm Thử
```
Types / Loại:
- Unit testing / Kiểm thử đơn vị
- Integration testing / Kiểm thử tích hợp
- Security testing / Kiểm thử bảo mật
- Penetration testing / Kiểm thử thâm nhập
```

## Lab Exercises / Bài Tập Thực Hành

### Basic Security / Bảo Mật Cơ Bản
1. SQL injection / Tiêm SQL
2. XSS attacks / Tấn công XSS
3. CSRF protection / Bảo vệ CSRF
4. Authentication bypass / Bỏ qua xác thực

### Advanced Security / Bảo Mật Nâng Cao
1. JWT implementation / Triển khai JWT
2. OAuth setup / Thiết lập OAuth
3. Security headers / Tiêu đề bảo mật
4. WAF configuration / Cấu hình WAF

### Security Assessment / Đánh Giá Bảo Mật
1. Vulnerability scanning / Quét lỗ hổng
2. Penetration testing / Kiểm thử thâm nhập
3. Code review / Đánh giá mã
4. Security audit / Kiểm toán bảo mật

## Assessment / Đánh Giá

### Quizzes / Kiểm Tra
- Multiple choice / Trắc nghiệm
- Vulnerability identification / Nhận diện lỗ hổng
- Attack analysis / Phân tích tấn công
- Security implementation / Triển khai bảo mật

### Projects / Dự Án
- Secure web application / Ứng dụng web an toàn
- Security assessment / Đánh giá bảo mật
- Penetration testing / Kiểm thử thâm nhập
- Security documentation / Tài liệu bảo mật

## Resources / Tài Nguyên

### Online Documentation / Tài Liệu Trực Tuyến
- OWASP Web Security
- MDN Web Security
- Web Security Testing Guide
- Security Headers

### Books / Sách
- "Web Application Security"
- "The Web Application Hacker's Handbook"
- "OWASP Testing Guide"
- "Web Security for Developers"

### Communities / Cộng Đồng
- OWASP Forums
- Web Security Stack Exchange
- Reddit /r/websecurity
- Security Forums

### Training / Đào Tạo
- OWASP Training
- PortSwigger Web Security Academy
- HackTheBox
- TryHackMe 