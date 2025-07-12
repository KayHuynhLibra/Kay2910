# Security & Compliance
# Bảo mật & Tuân thủ

## Overview / Tổng quan

This module covers essential security concepts and compliance frameworks for DevOps environments. You'll learn about security best practices, compliance requirements, and tools for implementing and maintaining secure systems.

Module này bao gồm các khái niệm bảo mật cơ bản và khung tuân thủ cho môi trường DevOps. Bạn sẽ học về các thực hành bảo mật tốt nhất, yêu cầu tuân thủ và công cụ để triển khai và duy trì hệ thống an toàn.

## Learning Objectives / Mục tiêu học tập

### 1. Security Fundamentals / Kiến thức cơ bản về bảo mật
- Security principles
- Threat modeling
- Vulnerability assessment
- Security controls
- Best practices

*Vietnamese:*
- Nguyên tắc bảo mật
- Mô hình hóa mối đe dọa
- Đánh giá lỗ hổng
- Kiểm soát bảo mật
- Thực hành tốt nhất

### 2. Compliance Frameworks / Khung tuân thủ
- Compliance requirements
- Audit procedures
- Documentation
- Risk management
- Best practices

*Vietnamese:*
- Yêu cầu tuân thủ
- Quy trình kiểm toán
- Tài liệu
- Quản lý rủi ro
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. Security Labs / Lab Bảo mật

#### Lab 1: Vulnerability Scanning / Quét lỗ hổng
```yaml
# trivy-config.yaml
scanners:
  - vuln
  - config
  - secret
  - license

severity: CRITICAL,HIGH

format: table

output: scan-results.txt

targets:
  - ./src
  - ./config
  - ./deployments
```

#### Lab 2: Security Policy / Chính sách bảo mật
```yaml
# security-policy.yaml
apiVersion: security.k8s.io/v1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  seLinux:
    rule: RunAsAny
  runAsUser:
    rule: MustRunAsNonRoot
  fsGroup:
    rule: MustRunAs
    ranges:
      - min: 1
        max: 65535
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'projected'
    - 'secret'
    - 'downwardAPI'
    - 'persistentVolumeClaim'
```

### 2. Compliance Labs / Lab Tuân thủ

#### Lab 1: Compliance Check / Kiểm tra tuân thủ
```yaml
# compliance-check.yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceCheck
metadata:
  name: security-baseline
spec:
  schedule: "0 0 * * *"
  rules:
    - name: password-policy
      description: "Check password policy compliance"
      check: |
        minlen = 12
        dcredit = -1
        ucredit = -1
        ocredit = -1
        lcredit = -1
    - name: file-permissions
      description: "Check file permissions"
      check: |
        mode = 0644
        owner = root
        group = root
```

#### Lab 2: Audit Logging / Ghi log kiểm toán
```yaml
# audit-config.yaml
apiVersion: audit.k8s.io/v1
kind: Policy
metadata:
  name: audit-policy
rules:
  - level: Metadata
    namespaces: ["kube-system"]
    verbs: ["get", "list", "watch"]
    resources:
      - group: ""
        resources: ["pods", "services"]
  - level: Request
    namespaces: ["default"]
    verbs: ["create", "update", "delete"]
    resources:
      - group: ""
        resources: ["secrets", "configmaps"]
```

## Projects / Dự án

### 1. Security Implementation / Triển khai bảo mật
- Security assessment
- Vulnerability management
- Security controls
- Monitoring

*Vietnamese:*
- Đánh giá bảo mật
- Quản lý lỗ hổng
- Kiểm soát bảo mật
- Giám sát

### 2. Compliance Framework / Khung tuân thủ
- Compliance assessment
- Documentation
- Audit procedures
- Risk management

*Vietnamese:*
- Đánh giá tuân thủ
- Tài liệu
- Quy trình kiểm toán
- Quản lý rủi ro

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- Security guides
- Compliance frameworks
- Best practices
- Case studies

*Vietnamese:*
- Hướng dẫn bảo mật
- Khung tuân thủ
- Thực hành tốt nhất
- Nghiên cứu tình huống

### 2. Tools / Công cụ
- Trivy
- OpenSCAP
- SonarQube
- OWASP ZAP

*Vietnamese:*
- Trivy
- OpenSCAP
- SonarQube
- OWASP ZAP

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- Security concepts
- Compliance requirements
- Tool usage
- Best practices

*Vietnamese:*
- Khái niệm bảo mật
- Yêu cầu tuân thủ
- Sử dụng công cụ
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Security assessment
- Compliance check
- Vulnerability scan
- Audit logging

*Vietnamese:*
- Đánh giá bảo mật
- Kiểm tra tuân thủ
- Quét lỗ hổng
- Ghi log kiểm toán

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- CompTIA Security+
- CISSP
- CISM
- AWS Certified Security - Specialty

*Vietnamese:*
- CompTIA Security+
- CISSP
- CISM
- AWS Certified Security - Specialty

### 2. Study Resources / Tài liệu học tập
- Official documentation
- Practice exams
- Study guides
- Online courses

*Vietnamese:*
- Tài liệu chính thức
- Bài thi thử
- Hướng dẫn học
- Khóa học trực tuyến

## Getting Started / Bắt đầu

1. **Prerequisites / Điều kiện tiên quyết**
   - Basic security knowledge
   - System administration
   - Networking concepts
   - Risk management

2. **Setup / Thiết lập**
   ```bash
   # Install Trivy
   curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

   # Install OpenSCAP
   sudo apt-get update
   sudo apt-get install openscap-utils
   ```

3. **Learning Path / Lộ trình học**
   - Start with security basics
   - Learn compliance concepts
   - Practice with tools
   - Implement solutions

## Contributing / Đóng góp

We welcome contributions to improve the course materials:
Chúng tôi hoan nghênh đóng góp để cải thiện tài liệu khóa học:

1. **Content Updates / Cập nhật nội dung**
   - Technical accuracy
   - Best practices
   - New features
   - Workflow improvements

2. **Translation / Dịch thuật**
   - English to Vietnamese
   - Vietnamese to English
   - Technical terminology

3. **Lab Improvements / Cải thiện Lab**
   - New exercises
   - Real-world scenarios
   - Troubleshooting guides

## Support / Hỗ trợ

For support and questions:
Để được hỗ trợ và giải đáp thắc mắc:

1. **Documentation / Tài liệu**
   - Course materials
   - Lab guides
   - Troubleshooting guides

2. **Community / Cộng đồng**
   - Discussion forums
   - Q&A sessions
   - Knowledge sharing

3. **Technical Support / Hỗ trợ kỹ thuật**
   - Issue reporting
   - Bug fixes
   - Feature requests 