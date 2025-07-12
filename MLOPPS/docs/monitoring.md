# Monitoring Guide

## Overview
Hướng dẫn thiết lập và quản lý hệ thống monitoring cho MLOps platform, bao gồm metrics collection, alerting, và visualization.

## Monitoring Stack

### Components
1. **Prometheus**
   - Metrics collection
   - Time series database
   - Alert management

2. **Grafana**
   - Metrics visualization
   - Dashboard management
   - Alert visualization

3. **AlertManager**
   - Alert routing
   - Alert grouping
   - Alert silencing

4. **Node Exporter**
   - System metrics
   - Hardware metrics
   - OS metrics

5. **cAdvisor**
   - Container metrics
   - Resource usage
   - Performance metrics

## Metrics Collection

### System Metrics
```yaml
# Node Exporter metrics
node_cpu_seconds_total
node_memory_MemTotal_bytes
node_filesystem_size_bytes
node_network_receive_bytes_total
node_network_transmit_bytes_total
```

### Application Metrics
```yaml
# API metrics
http_requests_total
http_request_duration_seconds
http_requests_in_flight
http_request_size_bytes
http_response_size_bytes
```

### Model Metrics
```yaml
# Model performance metrics
model_prediction_latency_seconds
model_prediction_requests_total
model_prediction_errors_total
model_accuracy
model_precision
model_recall
```

### Data Pipeline Metrics
```yaml
# Data processing metrics
data_processing_duration_seconds
data_processing_records_total
data_processing_errors_total
data_validation_errors_total
```

## Alerting Rules

### System Alerts
```yaml
# CPU usage alert
- alert: HighCPUUsage
  expr: 100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High CPU usage"
    description: "CPU usage is above 80% for 5 minutes"

# Memory usage alert
- alert: HighMemoryUsage
  expr: (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 > 85
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High memory usage"
    description: "Memory usage is above 85% for 5 minutes"
```

### Application Alerts
```yaml
# API latency alert
- alert: HighAPILatency
  expr: rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m]) > 1
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High API latency"
    description: "API latency is above 1 second for 5 minutes"

# Error rate alert
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate"
    description: "Error rate is above 5% for 5 minutes"
```

### Model Alerts
```yaml
# Model latency alert
- alert: HighModelLatency
  expr: rate(model_prediction_latency_seconds_sum[5m]) / rate(model_prediction_latency_seconds_count[5m]) > 0.5
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High model latency"
    description: "Model prediction latency is above 0.5 seconds for 5 minutes"

# Model accuracy alert
- alert: LowModelAccuracy
  expr: model_accuracy < 0.8
  for: 1h
  labels:
    severity: warning
  annotations:
    summary: "Low model accuracy"
    description: "Model accuracy is below 80% for 1 hour"
```

## Dashboards

### System Overview
```json
{
  "panels": [
    {
      "title": "CPU Usage",
      "type": "graph",
      "targets": [
        {
          "expr": "100 - (avg by(instance) (irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
        }
      ]
    },
    {
      "title": "Memory Usage",
      "type": "graph",
      "targets": [
        {
          "expr": "(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100"
        }
      ]
    }
  ]
}
```

### API Performance
```json
{
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(http_requests_total[5m])"
        }
      ]
    },
    {
      "title": "Response Time",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m])"
        }
      ]
    }
  ]
}
```

### Model Performance
```json
{
  "panels": [
    {
      "title": "Prediction Latency",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(model_prediction_latency_seconds_sum[5m]) / rate(model_prediction_latency_seconds_count[5m])"
        }
      ]
    },
    {
      "title": "Model Accuracy",
      "type": "gauge",
      "targets": [
        {
          "expr": "model_accuracy"
        }
      ]
    }
  ]
}
```

## Alert Management

### Alert Configuration
```yaml
# AlertManager configuration
route:
  group_by: ['alertname', 'instance']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'team-mlops'

receivers:
- name: 'team-mlops'
  email_configs:
  - to: 'mlops-team@example.com'
    send_resolved: true
  slack_configs:
  - channel: '#mlops-alerts'
    send_resolved: true
```

### Alert Routing
```yaml
# Alert routing rules
routes:
- match:
    severity: critical
  receiver: 'team-mlops-critical'
  continue: true

- match:
    severity: warning
  receiver: 'team-mlops-warning'
```

## Log Management

### Log Collection
```yaml
# Log collection configuration
scrape_configs:
- job_name: 'logs'
  static_configs:
  - targets: ['localhost:9090']
  relabel_configs:
  - source_labels: [__name__]
    regex: '.*_log.*'
    action: keep
```

### Log Analysis
```yaml
# Log analysis rules
rules:
- name: 'error_logs'
  expr: 'rate(error_logs_total[5m]) > 0'
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High error log rate"
    description: "Error log rate is above threshold for 5 minutes"
```

## Performance Monitoring

### Resource Monitoring
```yaml
# Resource monitoring rules
- name: 'resource_usage'
  expr: |
    node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes
    /
    node_memory_MemTotal_bytes * 100
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "High resource usage"
    description: "Resource usage is above threshold for 5 minutes"
```

### Performance Metrics
```yaml
# Performance metrics
- name: 'api_performance'
  expr: |
    rate(http_request_duration_seconds_sum[5m])
    /
    rate(http_request_duration_seconds_count[5m])
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "API performance degradation"
    description: "API response time is above threshold for 5 minutes"
```

## Security Monitoring

### Security Alerts
```yaml
# Security alert rules
- name: 'security_breach'
  expr: 'rate(security_violations_total[5m]) > 0'
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "Security breach detected"
    description: "Security violations detected in the last minute"
```

### Access Monitoring
```yaml
# Access monitoring rules
- name: 'unauthorized_access'
  expr: 'rate(unauthorized_access_attempts_total[5m]) > 0'
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "Unauthorized access attempts"
    description: "Unauthorized access attempts detected in the last minute"
```

## Best Practices

### Monitoring
- Set up comprehensive metrics collection
- Implement proper alerting rules
- Create informative dashboards
- Regular review of metrics and alerts
- Monitor system health proactively

### Alerting
- Use appropriate severity levels
- Configure proper alert routing
- Implement alert grouping
- Set up alert silencing
- Regular alert testing

### Visualization
- Create clear and informative dashboards
- Use appropriate visualization types
- Implement proper dashboard organization
- Regular dashboard updates
- Share dashboards with team

### Maintenance
- Regular metric review
- Alert rule optimization
- Dashboard updates
- Performance tuning
- Documentation updates 