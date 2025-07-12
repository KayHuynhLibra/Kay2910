# 20 Life Hacks dành cho DevOps Engineers

## Giới thiệu

Mẹo nghề, bí kíp, thủ thuật, bí mật nội bộ, cheat sheet hay best practices – gọi tên thế nào cũng được, ngành nào cũng có những thứ đó. Và bất kỳ ai làm nghề đủ lâu đều tích lũy cho mình một kho kỹ thuật riêng và những công cụ được mài giũa kỹ lưỡng để làm việc hiệu quả hơn.

## 1. Tooling

### 1.1 K9s
K9s là một giao diện người dùng (UI) chạy trên terminal để tương tác với các cụm Kubernetes.

**Tính năng nổi bật:**
- Duyệt Pod/Service/Deployment cực nhanh
- Xem logs thời gian thực
- Mô phỏng các kubectl exec ngay trên giao diện
- Tùy biến view, filter tài nguyên theo namespace, labels

**Cài đặt:**
```bash
# macOS
brew install k9s

# Linux
curl -sS https://webinstall.dev/k9s | bash

# Windows (Scoop)
scoop install k9s
```

### 1.2 tmux
Công cụ chia màn hình trong terminal, cho phép làm nhiều việc cùng lúc.

**Lệnh cơ bản:**
```bash
tmux                  # tạo phiên mới
tmux new -s ten       # tạo phiên có tên
Ctrl + b rồi d        # thoát phiên
tmux attach -t ten    # quay lại phiên
Ctrl + b rồi "        # chia khung ngang
Ctrl + b rồi %        # chia khung dọc
```

### 1.3 Glasskube
Trình quản lý gói mã nguồn mở dành cho Kubernetes.

**Điểm nổi bật:**
- Cú pháp thân thiện như Homebrew và npm
- Hỗ trợ cả UI lẫn CLI
- Tối ưu cho triển khai nhanh và cấu hình chuẩn

### 1.4 ripgrep
Công cụ tìm kiếm siêu nhanh trong dòng lệnh.

**Ưu điểm:**
- Tốc độ cực nhanh
- Hỗ trợ regex mạnh mẽ
- Tự động bỏ qua thư mục không cần thiết
- Tương thích đa nền tảng

### 1.5 Firefox Containers
Tiện ích quản lý nhiều tài khoản cloud cùng lúc.

**Tính năng:**
- Tách biệt phiên làm việc
- Bảo mật phiên làm việc
- Tùy chỉnh theo môi trường

### 1.6 VPA (Vertical Pod Autoscaler)
Tự động hóa cấu hình resource cho Pod.

**Cấu hình mẫu:**
```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind:       Deployment
    name:       my-app
  updatePolicy:
    updateMode: "Auto"
```

### 1.7 kctx và kubens
Bộ đôi command-line tool cho Kubernetes.

**Cài đặt:**
```bash
# Thay vì
kubectl config use-context my-prod-cluster
kubectl config set-context --current --namespace=team-a

# Chỉ cần
kctx my-prod-cluster
kubens team-a
```

## 2. Skills

### 2.1 Scripting
Kỹ năng sống còn cho DevOps.

**Ưu tiên học:**
- Bash
- Makefile
- Regex
- Python

### 2.2 Documentation
Ghi chép lại mọi thứ.

**Công cụ ghi chú phổ biến:**
- Notion
- Outline
- Obsidian
- Google Keep
- Joplin

## 3. Habits

### 3.1 Block Time thay vì To-Do List
- Đặt thời gian cụ thể cho từng công việc
- Tập trung làm việc không bị gián đoạn
- Cập nhật lịch trình khi cần

### 3.2 Reciprocal Meeting Blocks
- Dành thời gian deep work tương đương cho mỗi cuộc họp
- Giữ sự linh hoạt mà không ảnh hưởng đến thời gian tập trung

### 3.3 Quy trình kết thúc công việc
Checklist cuối ngày:
- Tập thể dục
- Giải quyết việc linh tinh
- Kiểm tra cuộc trò chuyện chưa kết thúc
- Lên kế hoạch cho ngày mai
- Viết nhật ký
- Kiểm tra chỉ số cuối ngày

### 3.4 Ghi chú trong cuộc họp
- Ghi chép và chia sẻ ghi chú sau họp
- Đảm bảo không bỏ sót chi tiết quan trọng

### 3.5 Test Run Outages
- Chuẩn bị ứng phó sự cố
- Làm quen với các tác vụ thiết yếu
- Cài đặt sẵn công cụ truy cập

## 4. Scripts, Configs và Extensions

### 4.1 Alias hữu ích
```bash
k=kubectl
kctx='kubectl ctx'
kgp='kubectl get pods'
kns='kubectl ns'
l='ls -lah'
la='ls -lAh'
ll='ls -lh'
ls='ls -G'
lsa='ls -lah'
md='mkdir -p'
rd=rmdir
run-help=man
```

### 4.2 TTL Controller
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: test-ttl-job
spec:
  ttlSecondsAfterFinished: 100
```

### 4.3 Git Sync Script
```bash
git remote add upstream <upstream-url>
git fetch upstream
git rebase upstream/main
git push --force-with-lease
```

### 4.4 Kubectl Auto Complete
```bash
# Linux
sudo apt-get install bash-completion
echo 'source <(kubectl completion bash)' >>~/.bashrc
source ~/.bashrc
```

### 4.5 Visual Studio Code Remote – SSH
Extension cho phép phát triển trên máy từ xa qua SSH.

## Kết luận

Không có công thức thần kỳ để trở thành DevOps top 1%. Đó là quá trình tích lũy kinh nghiệm, cải thiện công cụ, mài giũa kỹ năng và duy trì thói quen tốt. Hãy tập trung vào việc phát triển bản thân mỗi ngày. 