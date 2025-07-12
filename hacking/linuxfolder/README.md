# Linux Hacking Environment Setup

## Công cụ cơ bản cần thiết

### 1. Network Tools
- nmap - Network mapper và port scanner
- wireshark - Network protocol analyzer
- tcpdump - Network packet analyzer
- netcat - Network utility
- aircrack-ng - Wireless network security suite

### 2. Web Security Tools
- burpsuite - Web application security testing
- sqlmap - SQL injection testing
- nikto - Web server scanner
- dirb/dirbuster - Directory bruteforcer
- wfuzz - Web application fuzzer

### 3. Password Tools
- john the ripper - Password cracking
- hashcat - Advanced password recovery
- hydra - Network login cracker

### 4. Exploitation Tools
- metasploit framework - Penetration testing framework
- exploit-db - Database of exploits
- gdb - GNU debugger
- radare2 - Reverse engineering framework

### 5. Forensics Tools
- volatility - Memory forensics
- autopsy - Digital forensics platform
- binwalk - Firmware analysis tool

## Cài đặt trên Arch Linux

```bash
# Cập nhật hệ thống
sudo pacman -Syu

# Cài đặt các công cụ cơ bản
sudo pacman -S nmap wireshark-qt tcpdump netcat aircrack-ng

# Cài đặt các công cụ web security
sudo pacman -S burpsuite sqlmap nikto dirb wfuzz

# Cài đặt các công cụ password
sudo pacman -S john hashcat hydra

# Cài đặt các công cụ exploitation
sudo pacman -S metasploit exploit-db gdb radare2

# Cài đặt các công cụ forensics
sudo pacman -S volatility autopsy binwalk
```

## Cấu trúc thư mục đề xuất

```
linuxfolder/
├── tools/           # Các công cụ tùy chỉnh
├── exploits/        # Exploits và payloads
├── wordlists/       # Wordlists cho bruteforce
├── reports/         # Báo cáo pentest
├── targets/         # Thông tin về các mục tiêu
└── notes/           # Ghi chú và tài liệu
```

## Lưu ý quan trọng
1. Luôn sử dụng các công cụ này một cách có đạo đức và hợp pháp
2. Chỉ thực hiện pentest trên các hệ thống được phép
3. Giữ các công cụ luôn được cập nhật
4. Backup dữ liệu quan trọng
5. Sử dụng môi trường ảo hóa khi cần thiết 