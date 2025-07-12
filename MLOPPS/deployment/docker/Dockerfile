# Sử dụng Python 3.9 slim làm base image
FROM python:3.9-slim

# Thiết lập các biến môi trường
ENV PYTHONUNBUFFERED=1 \  # Không buffer output Python
    PYTHONDONTWRITEBYTECODE=1 \  # Không tạo .pyc files
    PIP_NO_CACHE_DIR=1 \  # Không cache pip packages
    PIP_DISABLE_PIP_VERSION_CHECK=1  # Không kiểm tra version pip

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các dependencies hệ thống
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \  # Các tools build
    curl \  # Công cụ network
    && rm -rf /var/lib/apt/lists/*  # Clean up

# Copy requirements file
COPY requirements.txt .

# Cài đặt Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ project
COPY . .

# Tạo các thư mục cần thiết
RUN mkdir -p /app/data/raw /app/data/processed /app/data/external \
    /app/models/production /app/models/experiments \
    /app/monitoring/metrics /app/monitoring/logs

# Thiết lập các biến môi trường
ENV MODEL_PATH=/app/models/production \  # Đường dẫn model
    DATA_PATH=/app/data \  # Đường dẫn data
    CONFIG_PATH=/app/configs  # Đường dẫn configs

# Expose port
EXPOSE 8000

# Chạy ứng dụng
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"] 