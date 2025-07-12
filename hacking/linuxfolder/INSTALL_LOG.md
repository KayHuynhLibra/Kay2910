# Log chi tiết quá trình cài đặt môi trường hacking trên Arch Linux

## 1. Tạo cấu trúc thư mục
```bash
mkdir -p linuxfolder/tools linuxfolder/exploits linuxfolder/wordlists linuxfolder/reports linuxfolder/targets linuxfolder/notes
```
- Đã tạo các thư mục con để tổ chức công cụ, exploits, wordlists, báo cáo, mục tiêu và ghi chú.

## 2. Tạo các file hướng dẫn và cấu hình
- **README.md**: Tổng quan môi trường, danh sách công cụ, hướng dẫn cài đặt.
- **INSTALL_STEPS.md**: Các bước cài đặt chi tiết, từng lệnh và lưu ý.
- **requirements.txt**: Thư viện Python cần thiết cho các tool tự động hóa, pentest.
- **setup.sh**: Script tự động cài đặt, có màu sắc cho dễ theo dõi.

## 3. Chạy script tự động hóa
```bash
cd linuxfolder
./setup.sh
```
- Script sẽ tự động cập nhật hệ thống, cài các gói cơ bản, tạo môi trường Python ảo, cài Python packages, tải wordlists, cấu hình Metasploit và Wireshark.
- Nếu script báo thiếu quyền, hãy kiểm tra quyền thực thi: `chmod +x setup.sh`

## 4. Lỗi và cách xử lý thực tế
### a. Thiếu wget và unzip khi tải wordlists
**Lỗi:**
```
./setup.sh: line 51: wget: command not found
./setup.sh: line 52: unzip: command not found
```
**Cách xử lý:**
```bash
sudo pacman -S wget unzip --noconfirm
```

### b. Thiếu postgresql và metasploit
**Lỗi:**
```
Failed to start postgresql.service: Unit postgresql.service not found.
sudo: msfdb: command not found
```
**Cách xử lý:**
```bash
sudo pacman -S postgresql metasploit --noconfirm
```

### c. Khởi tạo database cho PostgreSQL
**Lỗi:**
```
Job for postgresql.service failed because the control process exited with error code.
```
**Cách xử lý:**
```bash
sudo -u postgres initdb -D /var/lib/postgres/data
```

### d. Khởi động và enable PostgreSQL, khởi tạo Metasploit DB
**Lưu ý:**
- Chạy lệnh sau với user bình thường (không phải root):
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
msfdb init
```
- Output thành công:
```
Creating database at /home/USERNAME/.msf4/db
Database initialization successful
```

### e. Lựa chọn khi cài netcat
**Prompt:**
```
:: There are 2 providers available for netcat:
   1) gnu-netcat  2) openbsd-netcat
Enter a number (default=1):
```
- Chọn mặc định (1) hoặc nhập 1 rồi Enter.

### f. Một số gói không có trên pacman
**Lỗi:**
```
error: target not found: burpsuite
er...: target not found: dirb
error: target not found: wfuzz
error: target not found: exploit-db
error: target not found: autopsy
```
- Các gói này cần cài qua AUR hoặc tải thủ công.

## 5. Các lệnh kiểm tra sau cài đặt
```bash
nmap --version
msfconsole --version
python --version
pip list
```
- Đảm bảo các công cụ đã cài đặt thành công và hoạt động.

## 6. Tải wordlists thủ công nếu cần
```bash
cd linuxfolder/wordlists
wget https://github.com/danielmiessler/SecLists/archive/master.zip
unzip master.zip
mv SecLists-master/* .
rm -rf SecLists-master master.zip
cd ..
```
- Nếu script không tải được, hãy thực hiện thủ công các lệnh trên.

## 7. Ghi chú thực tế
- Một số công cụ như burpsuite, dirb, wfuzz, autopsy, exploit-db không có sẵn trên pacman, cần cài qua AUR (yay, paru, trizen...) hoặc tải thủ công.
- Nếu gặp lỗi với PostgreSQL, hãy đảm bảo đã initdb trước khi start service.
- Đăng xuất và đăng nhập lại để áp dụng quyền cho Wireshark (`sudo usermod -a -G wireshark $USER`).
- Kích hoạt môi trường Python ảo với: `source .venv/bin/activate` mỗi khi mở terminal mới.
- Để cập nhật các công cụ:
```bash
sudo pacman -Syu
pip list --outdated
pip install --upgrade -r requirements.txt
```

---

**File này lưu lại toàn bộ quá trình cài đặt, các lệnh đã chạy, output thực tế, lỗi và cách xử lý. Có thể dùng để tái hiện hoặc debug môi trường.** 