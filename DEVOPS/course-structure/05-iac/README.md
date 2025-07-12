# Infrastructure as Code (IaC)
# Cơ sở hạ tầng dưới dạng mã (IaC)

## Overview / Tổng quan

This module covers Infrastructure as Code principles and tools, focusing on Terraform and Ansible. You'll learn how to automate infrastructure provisioning, configuration management, and deployment processes.

Module này bao gồm các nguyên tắc và công cụ của Infrastructure as Code, tập trung vào Terraform và Ansible. Bạn sẽ học cách tự động hóa việc cung cấp cơ sở hạ tầng, quản lý cấu hình và quy trình triển khai.

## Learning Objectives / Mục tiêu học tập

### 1. Terraform Fundamentals / Kiến thức cơ bản về Terraform
- IaC concepts
- Terraform workflow
- Resource management
- State management
- Best practices

*Vietnamese:*
- Khái niệm IaC
- Quy trình làm việc với Terraform
- Quản lý tài nguyên
- Quản lý trạng thái
- Thực hành tốt nhất

### 2. Ansible Essentials / Kiến thức cơ bản về Ansible
- Configuration management
- Playbook development
- Role management
- Inventory management
- Best practices

*Vietnamese:*
- Quản lý cấu hình
- Phát triển playbook
- Quản lý role
- Quản lý inventory
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. Terraform Labs / Lab Terraform

#### Lab 1: Basic Infrastructure / Cơ sở hạ tầng cơ bản
```hcl
# main.tf
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "web-server"
  }
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web server"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

#### Lab 2: Module Development / Phát triển module
```hcl
# modules/network/main.tf
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
}

resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = cidrsubnet(var.vpc_cidr, 8, 1)

  tags = {
    Name = "public-subnet"
  }
}
```

### 2. Ansible Labs / Lab Ansible

#### Lab 1: Basic Playbook / Playbook cơ bản
```yaml
# playbook.yml
---
- name: Configure web server
  hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Configure nginx
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: restart nginx

  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted
```

#### Lab 2: Role Development / Phát triển role
```yaml
# roles/webserver/tasks/main.yml
---
- name: Install required packages
  apt:
    name: "{{ packages }}"
    state: present
    update_cache: yes
  vars:
    packages:
      - nginx
      - python3
      - python3-pip

- name: Install Python dependencies
  pip:
    name: "{{ requirements }}"
    state: present
  vars:
    requirements:
      - flask
      - gunicorn

- name: Configure web application
  template:
    src: templates/app.conf.j2
    dest: /etc/nginx/sites-available/app
  notify: restart nginx
```

## Projects / Dự án

### 1. Multi-Cloud Infrastructure / Cơ sở hạ tầng đa đám mây
- AWS and Azure setup
- Network configuration
- Security implementation
- Monitoring setup

*Vietnamese:*
- Thiết lập AWS và Azure
- Cấu hình mạng
- Triển khai bảo mật
- Thiết lập giám sát

### 2. Automated Deployment / Triển khai tự động
- Infrastructure provisioning
- Application deployment
- Configuration management
- Monitoring

*Vietnamese:*
- Cung cấp cơ sở hạ tầng
- Triển khai ứng dụng
- Quản lý cấu hình
- Giám sát

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- Terraform documentation
- Ansible guides
- Best practices
- Tutorials

*Vietnamese:*
- Tài liệu Terraform
- Hướng dẫn Ansible
- Thực hành tốt nhất
- Hướng dẫn

### 2. Tools / Công cụ
- Terraform
- Ansible
- Packer
- Vagrant

*Vietnamese:*
- Terraform
- Ansible
- Packer
- Vagrant

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- IaC concepts
- Terraform usage
- Ansible usage
- Best practices

*Vietnamese:*
- Khái niệm IaC
- Sử dụng Terraform
- Sử dụng Ansible
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Infrastructure setup
- Configuration management
- Module development
- Role creation

*Vietnamese:*
- Thiết lập cơ sở hạ tầng
- Quản lý cấu hình
- Phát triển module
- Tạo role

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- HashiCorp Certified: Terraform Associate
- Red Hat Certified Specialist in Ansible Automation
- AWS Certified DevOps Engineer
- Azure DevOps Engineer Expert

*Vietnamese:*
- HashiCorp Certified: Terraform Associate
- Red Hat Certified Specialist in Ansible Automation
- AWS Certified DevOps Engineer
- Azure DevOps Engineer Expert

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
   - Cloud platform knowledge
   - Basic scripting
   - YAML/JSON understanding
   - System administration

2. **Setup / Thiết lập**
   ```bash
   # Install Terraform
   curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
   sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
   sudo apt-get update && sudo apt-get install terraform

   # Install Ansible
   sudo apt update
   sudo apt install software-properties-common
   sudo apt-add-repository --yes --update ppa:ansible/ansible
   sudo apt install ansible
   ```

3. **Learning Path / Lộ trình học**
   - Start with Terraform basics
   - Learn Ansible concepts
   - Practice with tools
   - Implement infrastructure

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