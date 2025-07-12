# Bài tập 3: System Administration

## Mục tiêu
- Thực hành quản lý hệ thống
- Cấu hình và quản lý dịch vụ
- Monitoring và logging
- Bảo mật hệ thống

## Yêu cầu
1. Cấu hình và quản lý dịch vụ:
- Cài đặt và cấu hình Nginx
- Cài đặt và cấu hình MySQL
- Cài đặt và cấu hình Redis
- Tạo systemd service cho các ứng dụng

2. Monitoring và logging:
- Cài đặt và cấu hình Prometheus
- Cài đặt và cấu hình Grafana
- Cấu hình log rotation
- Tạo dashboard monitoring

3. Bảo mật hệ thống:
- Cấu hình firewall
- Cấu hình SELinux
- Tạo và quản lý SSL certificates
- Cấu hình SSH

## Hướng dẫn

### 1. Cấu hình Nginx
```bash
# Cài đặt Nginx
sudo apt update
sudo apt install nginx

# Cấu hình Nginx
sudo nano /etc/nginx/sites-available/myapp
```

```nginx
server {
    listen 80;
    server_name myapp.example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /static {
        root /var/www/myapp;
        expires 30d;
    }
}
```

```bash
# Kích hoạt site
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 2. Cấu hình MySQL
```bash
# Cài đặt MySQL
sudo apt install mysql-server

# Cấu hình bảo mật
sudo mysql_secure_installation

# Tạo database và user
sudo mysql
```

```sql
CREATE DATABASE myapp;
CREATE USER 'myapp'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myapp.* TO 'myapp'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Cấu hình Redis
```bash
# Cài đặt Redis
sudo apt install redis-server

# Cấu hình Redis
sudo nano /etc/redis/redis.conf
```

```conf
bind 127.0.0.1
port 6379
requirepass yourpassword
maxmemory 256mb
maxmemory-policy allkeys-lru
```

```bash
# Khởi động lại Redis
sudo systemctl restart redis
```

### 4. Systemd Service
```bash
# Tạo service file
sudo nano /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=MyApp Service
After=network.target mysql.service redis.service

[Service]
Type=simple
User=myapp
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/node app.js
Restart=always
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

```bash
# Kích hoạt service
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

### 5. Prometheus và Grafana
```bash
# Cài đặt Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.30.0/prometheus-2.30.0.linux-amd64.tar.gz
tar xvfz prometheus-*.tar.gz
cd prometheus-*

# Cấu hình Prometheus
nano prometheus.yml
```

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
  - job_name: 'mysql'
    static_configs:
      - targets: ['localhost:9104']
  - job_name: 'redis'
    static_configs:
      - targets: ['localhost:9121']
```

```bash
# Cài đặt Grafana
wget https://dl.grafana.com/oss/release/grafana_8.2.0_amd64.deb
sudo dpkg -i grafana_8.2.0_amd64.deb
sudo systemctl start grafana-server
```

### 6. Log Rotation
```bash
# Cấu hình log rotation
sudo nano /etc/logrotate.d/myapp
```

```
/var/log/myapp/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 myapp myapp
    sharedscripts
    postrotate
        systemctl reload myapp
    endscript
}
```

### 7. Firewall và SELinux
```bash
# Cấu hình firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# Cấu hình SELinux
sudo setenforce 1
sudo semanage port -a -t http_port_t -p tcp 3000
```

### 8. SSL Certificate
```bash
# Cài đặt Certbot
sudo apt install certbot python3-certbot-nginx

# Tạo certificate
sudo certbot --nginx -d myapp.example.com
```

### 9. SSH Configuration
```bash
# Cấu hình SSH
sudo nano /etc/ssh/sshd_config
```

```
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers myapp
```

```bash
# Khởi động lại SSH
sudo systemctl restart sshd
```

## Kiểm tra
1. Kiểm tra dịch vụ:
```bash
sudo systemctl status nginx
sudo systemctl status mysql
sudo systemctl status redis
sudo systemctl status myapp
```

2. Kiểm tra monitoring:
```bash
curl http://localhost:9090
curl http://localhost:3000
```

3. Kiểm tra bảo mật:
```bash
sudo ufw status
getenforce
sudo certbot certificates
```

## Gợi ý
- Sử dụng `systemctl` để quản lý dịch vụ
- Sử dụng `journalctl` để xem log
- Sử dụng `netstat` để kiểm tra port
- Sử dụng `ps` để kiểm tra tiến trình
- Sử dụng `top` để kiểm tra tài nguyên

## Tài liệu tham khảo
- Nginx Documentation
- MySQL Documentation
- Redis Documentation
- Prometheus Documentation
- Grafana Documentation
- Systemd Documentation 