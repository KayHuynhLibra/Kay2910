#!/bin/bash

# Bài tập 3: System Administration
# Tác giả: DevOps Team
# Ngày: 2024-03-15

# 1. Cài đặt và cấu hình Nginx
echo "1. Cài đặt và cấu hình Nginx..."
sudo apt update
sudo apt install -y nginx

# Tạo cấu hình Nginx
sudo tee /etc/nginx/sites-available/myapp << 'EOF'
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
EOF

# Kích hoạt site
sudo ln -sf /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# 2. Cài đặt và cấu hình MySQL
echo "2. Cài đặt và cấu hình MySQL..."
sudo apt install -y mysql-server

# Cấu hình bảo mật MySQL
sudo mysql_secure_installation << EOF
y
password
password
y
y
y
y
EOF

# Tạo database và user
sudo mysql << EOF
CREATE DATABASE myapp;
CREATE USER 'myapp'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myapp.* TO 'myapp'@'localhost';
FLUSH PRIVILEGES;
EOF

# 3. Cài đặt và cấu hình Redis
echo "3. Cài đặt và cấu hình Redis..."
sudo apt install -y redis-server

# Cấu hình Redis
sudo tee /etc/redis/redis.conf << 'EOF'
bind 127.0.0.1
port 6379
requirepass yourpassword
maxmemory 256mb
maxmemory-policy allkeys-lru
EOF

# Khởi động lại Redis
sudo systemctl restart redis

# 4. Tạo systemd service
echo "4. Tạo systemd service..."
sudo tee /etc/systemd/system/myapp.service << 'EOF'
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
EOF

# Tạo user và thư mục cho ứng dụng
sudo useradd -m -s /bin/bash myapp
sudo mkdir -p /var/www/myapp
sudo chown -R myapp:myapp /var/www/myapp

# Kích hoạt service
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp

# 5. Cài đặt và cấu hình Prometheus
echo "5. Cài đặt và cấu hình Prometheus..."
wget https://github.com/prometheus/prometheus/releases/download/v2.30.0/prometheus-2.30.0.linux-amd64.tar.gz
tar xvfz prometheus-*.tar.gz
cd prometheus-*

# Cấu hình Prometheus
tee prometheus.yml << 'EOF'
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
EOF

# Tạo systemd service cho Prometheus
sudo tee /etc/systemd/system/prometheus.service << 'EOF'
[Unit]
Description=Prometheus
After=network.target

[Service]
Type=simple
User=prometheus
ExecStart=/usr/local/bin/prometheus --config.file=/etc/prometheus/prometheus.yml
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Cài đặt Prometheus
sudo useradd -m -s /bin/bash prometheus
sudo mkdir -p /etc/prometheus
sudo cp prometheus.yml /etc/prometheus/
sudo cp prometheus promtool /usr/local/bin/
sudo chown -R prometheus:prometheus /etc/prometheus /usr/local/bin/prometheus

# Kích hoạt service
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus

# 6. Cài đặt và cấu hình Grafana
echo "6. Cài đặt và cấu hình Grafana..."
wget https://dl.grafana.com/oss/release/grafana_8.2.0_amd64.deb
sudo dpkg -i grafana_8.2.0_amd64.deb
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

# 7. Cấu hình log rotation
echo "7. Cấu hình log rotation..."
sudo tee /etc/logrotate.d/myapp << 'EOF'
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
EOF

# 8. Cấu hình firewall
echo "8. Cấu hình firewall..."
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# 9. Cấu hình SELinux
echo "9. Cấu hình SELinux..."
sudo setenforce 1
sudo semanage port -a -t http_port_t -p tcp 3000

# 10. Cài đặt và cấu hình SSL
echo "10. Cài đặt và cấu hình SSL..."
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d myapp.example.com

# 11. Cấu hình SSH
echo "11. Cấu hình SSH..."
sudo tee /etc/ssh/sshd_config << 'EOF'
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers myapp
EOF

# Khởi động lại SSH
sudo systemctl restart sshd

# Kiểm tra kết quả
echo "Kiểm tra kết quả..."
echo "1. Kiểm tra dịch vụ:"
sudo systemctl status nginx
sudo systemctl status mysql
sudo systemctl status redis
sudo systemctl status myapp
sudo systemctl status prometheus
sudo systemctl status grafana-server

echo "2. Kiểm tra monitoring:"
curl http://localhost:9090
curl http://localhost:3000

echo "3. Kiểm tra bảo mật:"
sudo ufw status
getenforce
sudo certbot certificates

echo "Hoàn thành!" 