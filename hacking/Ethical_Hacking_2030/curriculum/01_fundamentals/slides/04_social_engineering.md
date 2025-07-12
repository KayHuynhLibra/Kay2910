# Social Engineering / Kỹ Thuật Xã Hội

## Introduction / Giới Thiệu

### What is Social Engineering? / Kỹ Thuật Xã Hội là gì?
- Manipulation of human psychology / Thao túng tâm lý con người
- Information gathering / Thu thập thông tin
- Trust exploitation / Khai thác lòng tin
- Security bypass / Bỏ qua bảo mật

### Types of Social Engineering / Các Loại Kỹ Thuật Xã Hội
```
Phishing / Lừa đảo:
- Email phishing / Lừa đảo qua email
- Spear phishing / Lừa đảo có chủ đích
- Whaling / Lừa đảo cấp cao
- Vishing / Lừa đảo qua điện thoại

Pretexting / Giả danh:
- Identity creation / Tạo danh tính
- Scenario development / Phát triển kịch bản
- Information gathering / Thu thập thông tin
- Trust building / Xây dựng lòng tin

Baiting / Mồi nhử:
- Physical media / Phương tiện vật lý
- Digital media / Phương tiện số
- Free offers / Đề nghị miễn phí
- Curiosity exploitation / Khai thác tính tò mò
```

## Psychological Principles / Nguyên Tắc Tâm Lý

### Authority / Quyền Lực
```
- Position of power / Vị trí quyền lực
- Uniform or badge / Đồng phục hoặc thẻ
- Official appearance / Vẻ ngoài chính thức
- Command presence / Sự hiện diện mệnh lệnh
```

### Scarcity / Khan Hiếm
```
- Limited time / Thời gian giới hạn
- Limited quantity / Số lượng giới hạn
- Exclusive access / Truy cập độc quyền
- Urgency creation / Tạo sự khẩn cấp
```

### Reciprocity / Có Qua Có Lại
```
- Gift giving / Tặng quà
- Favor offering / Đề nghị giúp đỡ
- Information exchange / Trao đổi thông tin
- Relationship building / Xây dựng mối quan hệ
```

## Attack Vectors / Vectơ Tấn Công

### Email Attacks / Tấn Công Qua Email
```
- Spoofed addresses / Địa chỉ giả mạo
- Malicious attachments / Tệp đính kèm độc hại
- Phishing links / Liên kết lừa đảo
- Social proof / Bằng chứng xã hội
```

### Phone Attacks / Tấn Công Qua Điện Thoại
```
- Caller ID spoofing / Giả mạo ID người gọi
- Voice manipulation / Thao túng giọng nói
- Urgency creation / Tạo sự khẩn cấp
- Information gathering / Thu thập thông tin
```

### Physical Attacks / Tấn Công Vật Lý
```
- Tailgating / Đi theo
- Dumpster diving / Lục thùng rác
- Shoulder surfing / Nhìn trộm
- Badge cloning / Sao chép thẻ
```

## Tools and Techniques / Công Cụ và Kỹ Thuật

### OSINT Tools / Công Cụ OSINT
```
TheHarvester:
theHarvester -d domain.com -b all

Maltego:
maltego
# Create new graph and add domain

Recon-ng:
recon-ng
# Use modules for information gathering
```

### Phishing Tools / Công Cụ Lừa Đảo
```
SET (Social Engineering Toolkit):
setoolkit
# Select options:
# 1) Social-Engineering Attacks
# 2) Website Attack Vectors
# 3) Credential Harvester Attack Method

Gophish:
./gophish
# Access web interface at https://localhost:3333
```

### Email Tools / Công Cụ Email
```
Swaks:
swaks --to user@domain.com --from attacker@domain.com

EmailSpoofer:
python emailspoofer.py -t target@domain.com -f spoofed@domain.com
```

## Defense Strategies / Chiến Lược Phòng Thủ

### Awareness Training / Đào Tạo Nhận Thức
```
- Phishing awareness / Nhận thức về lừa đảo
- Social engineering awareness / Nhận thức về kỹ thuật xã hội
- Security policies / Chính sách bảo mật
- Incident reporting / Báo cáo sự cố
```

### Technical Controls / Kiểm Soát Kỹ Thuật
```
- Email filtering / Lọc email
- Web filtering / Lọc web
- Access controls / Kiểm soát truy cập
- Monitoring systems / Hệ thống giám sát
```

### Response Procedures / Quy Trình Phản Ứng
```
- Incident response / Phản ứng sự cố
- Reporting procedures / Quy trình báo cáo
- Recovery steps / Các bước khôi phục
- Post-incident analysis / Phân tích sau sự cố
```

## Ethical Considerations / Xem Xét Đạo Đức

### Legal Framework / Khung Pháp Lý
```
- Authorization requirements / Yêu cầu ủy quyền
- Privacy laws / Luật bảo mật
- Data protection / Bảo vệ dữ liệu
- Compliance requirements / Yêu cầu tuân thủ
```

### Professional Ethics / Đạo Đức Nghề Nghiệp
```
- Informed consent / Đồng ý có hiểu biết
- Data handling / Xử lý dữ liệu
- Confidentiality / Bảo mật
- Professional conduct / Hành vi chuyên nghiệp
```

## Lab Exercises / Bài Tập Thực Hành

### Basic Social Engineering / Kỹ Thuật Xã Hội Cơ Bản
1. Information gathering / Thu thập thông tin
2. Phishing campaign / Chiến dịch lừa đảo
3. Pretexting scenario / Kịch bản giả danh
4. Physical security test / Kiểm tra bảo mật vật lý

### Advanced Techniques / Kỹ Thuật Nâng Cao
1. Spear phishing / Lừa đảo có chủ đích
2. Social media exploitation / Khai thác mạng xã hội
3. Voice manipulation / Thao túng giọng nói
4. Multi-vector attacks / Tấn công đa vectơ

### Defense Implementation / Triển Khai Phòng Thủ
1. Security awareness program / Chương trình nhận thức bảo mật
2. Technical control deployment / Triển khai kiểm soát kỹ thuật
3. Incident response testing / Kiểm tra phản ứng sự cố
4. Policy development / Phát triển chính sách

## Assessment / Đánh Giá

### Quizzes / Kiểm Tra
- Multiple choice / Trắc nghiệm
- Scenario analysis / Phân tích kịch bản
- Role-playing / Đóng vai
- Case studies / Nghiên cứu tình huống

### Projects / Dự Án
- Security assessment / Đánh giá bảo mật
- Awareness program / Chương trình nhận thức
- Policy development / Phát triển chính sách
- Incident response plan / Kế hoạch phản ứng sự cố

## Resources / Tài Nguyên

### Online Documentation / Tài Liệu Trực Tuyến
- Social-Engineer.org
- Phishing.org
- SANS Social Engineering
- OWASP Social Engineering

### Books / Sách
- "The Art of Deception"
- "Social Engineering: The Science of Human Hacking"
- "No Tech Hacking"
- "Social Engineering in IT Security"

### Communities / Cộng Đồng
- Social-Engineer.org Forums
- Reddit /r/SocialEngineering
- LinkedIn Groups
- Security Forums

### Training / Đào Tạo
- KnowBe4
- PhishMe
- Wombat Security
- SecurityIQ 