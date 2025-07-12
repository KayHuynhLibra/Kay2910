# Monitoring & Logging
# Giám sát & Ghi log

## Overview / Tổng quan

This module covers monitoring and logging solutions for DevOps environments. You'll learn about Prometheus, Grafana, ELK Stack, and other tools for collecting, analyzing, and visualizing metrics and logs.

Module này bao gồm các giải pháp giám sát và ghi log cho môi trường DevOps. Bạn sẽ học về Prometheus, Grafana, ELK Stack và các công cụ khác để thu thập, phân tích và trực quan hóa metrics và logs.

## Learning Objectives / Mục tiêu học tập

### 1. Monitoring Fundamentals / Kiến thức cơ bản về giám sát
- Metrics collection
- Alerting
- Visualization
- Performance monitoring
- Best practices

*Vietnamese:*
- Thu thập metrics
- Cảnh báo
- Trực quan hóa
- Giám sát hiệu suất
- Thực hành tốt nhất

### 2. Logging Essentials / Kiến thức cơ bản về ghi log
- Log collection
- Log analysis
- Log storage
- Log visualization
- Best practices

*Vietnamese:*
- Thu thập log
- Phân tích log
- Lưu trữ log
- Trực quan hóa log
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. Monitoring Labs / Lab Giám sát

#### Lab 1: Prometheus Setup / Thiết lập Prometheus
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

rule_files:
  - "rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

#### Lab 2: Grafana Dashboard / Dashboard Grafana
```json
{
  "annotations": {
    "list": []
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "title": "CPU Usage",
      "type": "timeseries"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 38,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "System Overview",
  "version": 0,
  "weekStart": ""
}
```

### 2. Logging Labs / Lab Ghi log

#### Lab 1: ELK Stack Setup / Thiết lập ELK Stack
```yaml
# logstash.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGBASE} %{GREEDYDATA:syslog_message}" }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
```

#### Lab 2: Log Analysis / Phân tích log
```json
{
  "index_patterns": ["logs-*"],
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "@timestamp": {
        "type": "date"
      },
      "message": {
        "type": "text"
      },
      "host": {
        "type": "keyword"
      },
      "level": {
        "type": "keyword"
      }
    }
  }
}
```

## Projects / Dự án

### 1. Monitoring Solution / Giải pháp giám sát
- Metrics collection
- Alerting setup
- Dashboard creation
- Performance analysis

*Vietnamese:*
- Thu thập metrics
- Thiết lập cảnh báo
- Tạo dashboard
- Phân tích hiệu suất

### 2. Logging Solution / Giải pháp ghi log
- Log collection
- Log analysis
- Log storage
- Log visualization

*Vietnamese:*
- Thu thập log
- Phân tích log
- Lưu trữ log
- Trực quan hóa log

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- Prometheus documentation
- Grafana guides
- ELK Stack guides
- Best practices

*Vietnamese:*
- Tài liệu Prometheus
- Hướng dẫn Grafana
- Hướng dẫn ELK Stack
- Thực hành tốt nhất

### 2. Tools / Công cụ
- Prometheus
- Grafana
- ELK Stack
- AlertManager

*Vietnamese:*
- Prometheus
- Grafana
- ELK Stack
- AlertManager

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- Monitoring concepts
- Logging concepts
- Tool usage
- Best practices

*Vietnamese:*
- Khái niệm giám sát
- Khái niệm ghi log
- Sử dụng công cụ
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Monitoring setup
- Logging setup
- Dashboard creation
- Alert configuration

*Vietnamese:*
- Thiết lập giám sát
- Thiết lập ghi log
- Tạo dashboard
- Cấu hình cảnh báo

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- Prometheus Certified Associate
- Grafana Certified
- Elastic Certified Engineer
- AWS Certified DevOps Engineer

*Vietnamese:*
- Prometheus Certified Associate
- Grafana Certified
- Elastic Certified Engineer
- AWS Certified DevOps Engineer

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
   - Basic Linux knowledge
   - Networking concepts
   - System administration
   - Data analysis

2. **Setup / Thiết lập**
   ```bash
   # Install Prometheus
   wget https://github.com/prometheus/prometheus/releases/download/v2.30.0/prometheus-2.30.0.linux-amd64.tar.gz
   tar xvfz prometheus-*.tar.gz
   cd prometheus-*

   # Install Grafana
   sudo apt-get install -y apt-transport-https
   sudo apt-get install -y software-properties-common wget
   wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
   echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
   sudo apt-get update
   sudo apt-get install grafana
   ```

3. **Learning Path / Lộ trình học**
   - Start with monitoring basics
   - Learn logging concepts
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