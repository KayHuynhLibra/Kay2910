# Các bước cài đặt và cấu hình môi trường hacking

## 1. Cập nhật hệ thống
```bash
sudo pacman -Syu
```

## 2. Cài đặt các công cụ cơ bản
```bash
sudo pacman -S nmap wireshark-qt tcpdump netcat aircrack-ng
```

## 3. Cài đặt các công cụ web security
```bash
sudo pacman -S burpsuite sqlmap nikto dirb wfuzz
```

## 4. Cài đặt các công cụ password
```bash
sudo pacman -S john hashcat hydra
```

## 5. Cài đặt các công cụ exploitation
```bash
sudo pacman -S metasploit exploit-db gdb radare2
```

## 6. Cài đặt các công cụ forensics
```bash
sudo pacman -S volatility autopsy binwalk
```

## 7. Cài đặt các công cụ bổ sung
```bash
sudo pacman -S python-pip python-virtualenv git
```

## 8. Tạo môi trường Python ảo
```bash
python -m venv .venv
source .venv/bin/activate
```

## 9. Cài đặt các thư viện Python cần thiết
```bash
pip install requests beautifulsoup4 paramiko scapy
```

## 10. Tải các wordlist phổ biến
```bash
cd wordlists
wget https://github.com/danielmiessler/SecLists/archive/master.zip
unzip master.zip
mv SecLists-master/* .
rm -rf SecLists-master master.zip
cd ..
```

## 11. Cấu hình Metasploit
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo msfdb init
```

## 12. Cấu hình Wireshark
```bash
sudo usermod -a -G wireshark $USER
```

## 13. Kiểm tra cài đặt
```bash
# Kiểm tra nmap
nmap --version

# Kiểm tra metasploit
msfconsole --version

# Kiểm tra python
python --version
pip list
```

## Lưu ý sau khi cài đặt
1. Đăng xuất và đăng nhập lại để áp dụng các thay đổi về quyền
2. Chạy `source .venv/bin/activate` mỗi khi mở terminal mới
3. Cập nhật các công cụ thường xuyên:
   ```bash
   sudo pacman -Syu
   pip list --outdated
   pip install --upgrade -r requirements.txt
   ``` 