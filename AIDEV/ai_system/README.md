# Hệ Thống AI Tự Động Hóa

Đây là một hệ thống AI hoàn chỉnh kết hợp nhiều agent thông minh để tự động hóa các tác vụ và tương tác với người dùng.

## Cấu Trúc Dự Án

```
ai_system/
├── agents/                 # Thư mục chứa các AI agents
│   ├── base_agent.py      # Lớp cơ sở cho tất cả agents
│   ├── chat_agent.py      # Agent xử lý chat
│   ├── task_agent.py      # Agent xử lý tác vụ
│   └── coordinator.py     # Agent điều phối
├── api/                   # API endpoints
│   ├── routes/           # Các route handlers
│   └── models.py         # Data models
├── core/                 # Core functionality
│   ├── config.py        # Cấu hình hệ thống
│   ├── security.py      # Bảo mật
│   └── database.py      # Database models
├── utils/               # Utility functions
├── main.py             # Entry point
└── requirements.txt    # Dependencies
```

## Tính Năng Chính

1. **Multi-Agent System**
   - Chat Agent: Xử lý tương tác với người dùng
   - Task Agent: Thực hiện các tác vụ tự động
   - Coordinator: Điều phối giữa các agents

2. **Tự Động Hóa**
   - Tự động phân tích và xử lý tác vụ
   - Tích hợp với các API bên ngoài
   - Lập lịch và thực hiện tác vụ

3. **Bảo Mật**
   - Authentication và Authorization
   - API key management
   - Rate limiting

4. **Database**
   - Lưu trữ lịch sử tương tác
   - Quản lý người dùng
   - Lưu trữ dữ liệu tác vụ

## Cài Đặt

1. Tạo môi trường ảo:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Cấu hình môi trường:
- Copy `.env.example` thành `.env`
- Cập nhật các biến môi trường cần thiết

4. Khởi tạo database:
```bash
python scripts/init_db.py
```

## Chạy Ứng Dụng

1. Chạy server:
```bash
python main.py
```

2. Truy cập API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

1. **Authentication**
   - POST /auth/token
   - POST /auth/refresh

2. **Chat**
   - POST /chat/send
   - GET /chat/history

3. **Tasks**
   - POST /tasks/create
   - GET /tasks/list
   - GET /tasks/{task_id}

4. **System**
   - GET /system/status
   - GET /system/metrics

## Phát Triển

1. **Thêm Agent Mới**
   - Kế thừa từ BaseAgent
   - Implement các phương thức cần thiết
   - Đăng ký với Coordinator

2. **Tích Hợp API**
   - Thêm route mới trong api/routes
   - Cập nhật models nếu cần
   - Thêm validation và error handling

3. **Testing**
   - Unit tests: `pytest tests/unit`
   - Integration tests: `pytest tests/integration`
   - API tests: `pytest tests/api`

## Monitoring

1. **Logs**
   - Application logs: `logs/app.log`
   - Error logs: `logs/error.log`
   - Access logs: `logs/access.log`

2. **Metrics**
   - System metrics: `/system/metrics`
   - Agent performance: `/agents/metrics`
   - API usage: `/api/metrics`

## Contributing

1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Push lên branch
5. Tạo Pull Request

## License

MIT License

# Chat History System

A robust system for storing, managing, and analyzing chat history with scheduled maintenance tasks and comprehensive monitoring.

## Features

- Daily file rotation for chat history
- Automatic cleanup of old history
- Scheduled backups and reports
- Real-time metrics and monitoring
- Thread-safe operations
- Comprehensive error handling
- Configurable retention policies
- RESTful API endpoints
- Prometheus metrics integration
- Grafana dashboards

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export CHAT_HISTORY_DIR="data/chat_history"
export CHAT_HISTORY_ENCRYPTION_KEY="your-encryption-key"
```

3. Start the service:
```bash
uvicorn ai_system.api.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Message Management

- `POST /chat-history/messages` - Add a new message
- `GET /chat-history/history/{date}` - Get chat history for a specific date
- `GET /chat-history/user/{user_id}` - Get user's chat history
- `GET /chat-history/search` - Search messages with filters

### Analytics

- `GET /chat-history/statistics/{date}` - Get statistics for a specific date
- `GET /chat-history/analytics/daily` - Get detailed daily analytics
- `GET /chat-history/analytics/trends` - Get trend analysis
- `GET /chat-history/users/active` - Get active users list
- `GET /chat-history/users/{user_id}/activity` - Get user activity metrics

### System Management

- `GET /chat-history/scheduled-tasks` - List scheduled tasks
- `POST /chat-history/schedule-task` - Schedule a new task
- `DELETE /chat-history/scheduled-tasks/{task_name}` - Remove a scheduled task
- `POST /chat-history/export` - Export chat history
- `POST /chat-history/backup/restore` - Restore from backup
- `GET /chat-history/health` - System health check

## Usage Examples

### Adding Messages

```python
import requests

# Add a new message
response = requests.post(
    "http://localhost:8000/chat-history/messages",
    json={
        "user_id": "user123",
        "message": "Hello, world!",
        "response": "Hi there!",
        "metadata": {"type": "greeting"}
    },
    headers={"Authorization": "Bearer your-token"}
)
```

### Retrieving History

```python
# Get today's history
response = requests.get(
    "http://localhost:8000/chat-history/history/2024-03-20",
    headers={"Authorization": "Bearer your-token"}
)

# Get user history
response = requests.get(
    "http://localhost:8000/chat-history/user/user123?days=7",
    headers={"Authorization": "Bearer your-token"}
)
```

### Scheduling Tasks

```python
# Schedule a daily cleanup task
response = requests.post(
    "http://localhost:8000/chat-history/schedule-task",
    json={
        "name": "daily_cleanup",
        "schedule_time": "00:00",
        "task_type": "cleanup"
    },
    headers={"Authorization": "Bearer your-token"}
)
```

## Monitoring

The system exposes Prometheus metrics at `/metrics` and includes a Grafana dashboard for visualization.

### Key Metrics

- Message rate
- Active users
- Response time
- Error rate
- Storage usage
- Scheduled tasks

### Grafana Dashboard

Import the dashboard from `grafana/dashboards/chat_history_metrics.json` to visualize:

1. Message Rate Panel
2. Active Users Panel
3. Response Time Panel
4. Error Rate Panel
5. Storage Usage Panel
6. Scheduled Tasks Panel

## Configuration

Configuration options are available in `ai_system/config/chat_history_config.py`:

- Storage paths
- Retention periods
- Schedule times
- Security settings
- Rate limiting
- Cache settings
- Monitoring settings

## Security

- Authentication required for all endpoints
- Role-based access control
- Rate limiting
- Encrypted backups
- Secure file handling

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
black ai_system/
flake8 ai_system/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Advanced Analytics Examples

### Sentiment Analysis

```python
# Get sentiment analysis for a specific date
response = requests.get(
    "http://localhost:8000/chat-history/analytics/sentiment/2024-03-20",
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "date": "2024-03-20",
    "overall_sentiment": {
        "positive": 0.65,
        "negative": 0.15,
        "neutral": 0.20
    },
    "hourly_sentiment": [
        {
            "hour": 9,
            "positive": 0.70,
            "negative": 0.10,
            "neutral": 0.20
        }
    ],
    "top_positive_topics": ["support", "features", "updates"],
    "top_negative_topics": ["bugs", "performance"]
}
```

### User Engagement Analysis

```python
# Get detailed engagement metrics for a user
response = requests.get(
    "http://localhost:8000/chat-history/analytics/engagement/user123?days=7",
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "user_id": "user123",
    "engagement_score": 0.85,
    "message_frequency": {
        "daily": 15,
        "weekly": 105
    },
    "response_time_trend": [
        {
            "date": "2024-03-20",
            "avg_response_time": 2.5
        }
    ],
    "active_hours": [9, 10, 11, 14, 15, 16],
    "conversation_depth": 3.2,
    "topic_preferences": ["technical", "support", "features"]
}
```

### Conversation Flow Analysis

```python
# Analyze conversation patterns
response = requests.get(
    "http://localhost:8000/chat-history/analytics/conversation-flow?date=2024-03-20&min_duration=300",
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "date": "2024-03-20",
    "conversations": [
        {
            "topic": "technical_support",
            "duration": 450,
            "participant_count": 3,
            "message_count": 25,
            "sentiment_trend": [0.6, 0.7, 0.8]
        }
    ],
    "topic_distribution": {
        "technical_support": 0.4,
        "feature_requests": 0.3,
        "bug_reports": 0.3
    },
    "average_duration": 380,
    "participant_patterns": {
        "2_participants": 0.6,
        "3_participants": 0.3,
        "4+_participants": 0.1
    },
    "sentiment_trends": [
        {
            "hour": 9,
            "sentiment": 0.75
        }
    ]
}
```

### Peak Hours Analysis

```python
# Get peak activity hours
response = requests.get(
    "http://localhost:8000/chat-history/analytics/peak-hours?days=7",
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "peak_hours": [10, 11, 14, 15],
    "activity_distribution": {
        "morning": 0.3,
        "afternoon": 0.5,
        "evening": 0.2
    },
    "weekday_vs_weekend": {
        "weekday": 0.8,
        "weekend": 0.2
    },
    "trend": [
        {
            "date": "2024-03-20",
            "peak_hour": 11,
            "activity_level": 0.85
        }
    ]
}
```

### Message Quality Analysis

```python
# Get message quality metrics
response = requests.get(
    "http://localhost:8000/chat-history/analytics/message-quality/2024-03-20",
    params={"min_messages": 10},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "date": "2024-03-20",
    "overall_quality": {
        "clarity": 0.85,
        "relevance": 0.92,
        "satisfaction": 0.88
    },
    "hourly_metrics": [
        {
            "hour": 9,
            "clarity": 0.87,
            "relevance": 0.90,
            "satisfaction": 0.85
        }
    ],
    "top_quality_topics": ["technical_support", "feature_requests"],
    "improvement_areas": ["response_time", "complexity"],
    "user_feedback": {
        "positive": 150,
        "negative": 20,
        "neutral": 30
    }
}
```

### User Behavior Analysis

```python
# Get user behavior analysis
response = requests.get(
    "http://localhost:8000/chat-history/analytics/user-behavior/user123",
    params={"days": 7},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "user_id": "user123",
    "behavior_patterns": {
        "session_duration": 45.5,
        "message_complexity": 0.75,
        "interaction_frequency": 12.3,
        "topic_preferences": ["technical", "support"]
    },
    "engagement_metrics": {
        "active_days": 5,
        "avg_messages_per_day": 15.2,
        "peak_activity_hours": [10, 11, 14]
    },
    "learning_curve": {
        "complexity_trend": [0.5, 0.6, 0.7, 0.75],
        "topic_diversity": 0.8,
        "skill_progression": 0.85
    },
    "interaction_quality": {
        "response_accuracy": 0.92,
        "conversation_depth": 3.5,
        "satisfaction_score": 0.88
    }
}
```

### System Performance Analysis

```python
# Get system performance metrics
response = requests.get(
    "http://localhost:8000/chat-history/analytics/system-performance",
    params={"time_range": "1h"},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "response_times": {
        "p50": 0.15,
        "p90": 0.25,
        "p95": 0.35,
        "p99": 0.50
    },
    "error_rates": {
        "total": 0.02,
        "by_type": {
            "validation": 0.01,
            "processing": 0.005,
            "storage": 0.005
        },
        "trend": [
            {
                "timestamp": "2024-03-20T10:00:00Z",
                "rate": 0.02
            }
        ]
    },
    "resource_usage": {
        "cpu": 45.5,
        "memory": 60.2,
        "disk": 75.8,
        "network": 30.5
    },
    "cache_performance": {
        "hit_rate": 0.85,
        "miss_rate": 0.15,
        "eviction_rate": 0.05
    },
    "concurrent_users": {
        "current": 150,
        "peak": 200,
        "average": 120.5
    }
}
```

### Topic Evolution Analysis

```python
# Get topic evolution analysis
response = requests.get(
    "http://localhost:8000/chat-history/analytics/topic-evolution",
    params={"days": 30, "min_occurrences": 5},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "topic_trends": [
        {
            "topic": "technical_support",
            "trend": [0.3, 0.35, 0.4, 0.45],
            "growth_rate": 0.15
        }
    ],
    "emerging_topics": [
        {
            "topic": "new_feature",
            "first_seen": "2024-03-15",
            "growth_rate": 0.25
        }
    ],
    "declining_topics": [
        {
            "topic": "legacy_feature",
            "decline_rate": 0.1
        }
    ],
    "topic_correlations": {
        "technical_support": ["performance", "bug_reports"],
        "feature_requests": ["usability", "design"]
    },
    "seasonal_patterns": {
        "weekday": {
            "morning": ["technical", "support"],
            "afternoon": ["features", "design"]
        },
        "weekend": {
            "morning": ["general", "feedback"],
            "afternoon": ["bugs", "issues"]
        }
    },
    "user_interest_shifts": [
        {
            "from_topic": "basic_features",
            "to_topic": "advanced_features",
            "shift_rate": 0.2
        }
    ]
}
```

## Monitoring Dashboard

The enhanced Grafana dashboard now includes:

1. **Message Quality Metrics**
   - Clarity score
   - Relevance score
   - User satisfaction
   - Quality trends

2. **User Behavior Analysis**
   - Message complexity
   - Session duration
   - Topic switching frequency
   - Interaction patterns

3. **System Performance Metrics**
   - Response time percentiles
   - Error rates
   - Resource usage
   - Cache performance

4. **Topic Evolution Analysis**
   - Topic trends
   - Emerging topics
   - Declining topics
   - Topic correlations

## Security Features

The system implements several security measures:

1. **Authentication**
   - JWT-based authentication
   - Role-based access control
   - Token refresh mechanism

2. **Rate Limiting**
   - Per-user rate limits
   - IP-based rate limiting
   - Burst handling

3. **Data Protection**
   - Encrypted storage
   - Secure backups
   - Data retention policies

4. **API Security**
   - Input validation
   - SQL injection prevention
   - XSS protection

Example security configuration:

```python
# Security settings
SECURITY_CONFIG = {
    "jwt_secret": "your-secret-key",
    "token_expiry": 3600,  # 1 hour
    "refresh_token_expiry": 604800,  # 7 days
    "rate_limit": {
        "requests": 100,
        "period": 60  # per minute
    },
    "encryption": {
        "algorithm": "AES-256-GCM",
        "key_rotation": 30  # days
    }
}
```

## Development Guidelines

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints
   - Document all functions

2. **Testing**
   - Write unit tests for all new features
   - Include integration tests
   - Maintain test coverage

3. **Performance**
   - Use async/await for I/O operations
   - Implement caching where appropriate
   - Monitor memory usage

4. **Error Handling**
   - Use custom exception classes
   - Implement proper logging
   - Provide meaningful error messages

Example test case:

```python
def test_message_quality_analysis():
    """Test message quality analysis endpoint."""
    response = client.get(
        "/chat-history/analytics/message-quality/2024-03-20",
        params={"min_messages": 10},
        headers={"Authorization": f"Bearer {test_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "overall_quality" in data
    assert "hourly_metrics" in data
    assert "top_quality_topics" in data
```

## Advanced Analytics Examples

### Message Pattern Analysis

```python
# Get message pattern analysis
response = requests.get(
    "http://localhost:8000/chat-history/analytics/message-patterns/2024-03-20",
    params={"min_frequency": 0.1},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "date": "2024-03-20",
    "patterns": [
        {
            "pattern_type": "greeting",
            "frequency": 0.25,
            "context": {
                "morning": 0.4,
                "afternoon": 0.3,
                "evening": 0.3
            },
            "time_distribution": [
                {
                    "hour": 9,
                    "frequency": 0.15
                }
            ]
        }
    ],
    "pattern_correlations": {
        "greeting": ["farewell", "question"],
        "question": ["answer", "clarification"]
    },
    "context_analysis": {
        "time_based": {},
        "user_based": {},
        "topic_based": {}
    }
}
```

### User Interaction Analysis

```python
# Get user interaction analysis
response = requests.get(
    "http://localhost:8000/chat-history/analytics/user-interactions/user123",
    params={"days": 7},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "user_id": "user123",
    "interactions": [
        {
            "interaction_type": "task_completion",
            "success_rate": 0.85,
            "average_duration": 120.5,
            "completion_rate": 0.92
        }
    ],
    "interaction_flow": {
        "start_points": ["greeting", "question"],
        "end_points": ["farewell", "confirmation"],
        "common_paths": [
            ["greeting", "question", "answer", "farewell"]
        ]
    },
    "success_metrics": {
        "overall_success": 0.88,
        "by_type": {},
        "by_time": {},
        "by_topic": {}
    }
}
```

### System Health Analysis

```python
# Get system health metrics
response = requests.get(
    "http://localhost:8000/chat-history/analytics/system-health",
    params={"components": ["chat_history", "database", "cache"]},
    headers={"Authorization": "Bearer your-token"}
)

# Example response
{
    "overall_status": "healthy",
    "components": [
        {
            "component": "chat_history",
            "status": "healthy",
            "metrics": {
                "storage_usage": 75.5,
                "response_time": 0.15,
                "error_rate": 0.02
            },
            "alerts": [
                {
                    "level": "warning",
                    "message": "Storage usage approaching limit",
                    "timestamp": "2024-03-20T10:00:00Z"
                }
            ]
        }
    ],
    "dependencies": {
        "database": "healthy",
        "cache": "healthy",
        "storage": "warning"
    },
    "performance_metrics": {
        "cpu_usage": 45.5,
        "memory_usage": 60.2,
        "disk_usage": 75.8,
        "network_usage": 30.5
    },
    "alerts_summary": {
        "critical": 0,
        "warning": 1,
        "info": 2
    }
}
```

## Enhanced Monitoring Dashboard

The Grafana dashboard now includes additional panels for:

1. **Message Pattern Analysis**
   - Pattern frequency
   - Pattern correlations
   - Context-based distribution

2. **User Interaction Metrics**
   - Success rates
   - Completion rates
   - Interaction duration

3. **System Health Status**
   - Component status
   - Alert counts
   - Performance metrics

## Security Features

The system implements enhanced security measures:

1. **Authentication**
   - JWT-based authentication
   - Role-based access control
   - Token refresh mechanism
   - Session management

2. **Rate Limiting**
   - Per-user rate limits
   - IP-based rate limiting
   - Burst handling
   - Concurrent request limits

3. **Data Protection**
   - Encrypted storage
   - Secure backups
   - Data retention policies
   - Data anonymization

4. **API Security**
   - Input validation
   - SQL injection prevention
   - XSS protection
   - CSRF protection

Example security configuration:

```python
# Enhanced security settings
SECURITY_CONFIG = {
    "jwt": {
        "secret": "your-secret-key",
        "algorithm": "HS256",
        "token_expiry": 3600,  # 1 hour
        "refresh_token_expiry": 604800,  # 7 days
        "refresh_token_rotation": True
    },
    "rate_limiting": {
        "requests": 100,
        "period": 60,  # per minute
        "burst": 20,
        "concurrent": 10
    },
    "encryption": {
        "algorithm": "AES-256-GCM",
        "key_rotation": 30,  # days
        "backup_encryption": True
    },
    "session": {
        "max_sessions": 5,
        "inactivity_timeout": 1800,  # 30 minutes
        "force_logout": True
    }
}
```

## Development Guidelines

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints
   - Document all functions
   - Use meaningful variable names

2. **Testing**
   - Write unit tests for all new features
   - Include integration tests
   - Maintain test coverage
   - Use test fixtures

3. **Performance**
   - Use async/await for I/O operations
   - Implement caching where appropriate
   - Monitor memory usage
   - Optimize database queries

4. **Error Handling**
   - Use custom exception classes
   - Implement proper logging
   - Provide meaningful error messages
   - Handle edge cases

Example test case:

```python
def test_message_pattern_analysis():
    """Test message pattern analysis endpoint."""
    response = client.get(
        "/chat-history/analytics/message-patterns/2024-03-20",
        params={"min_frequency": 0.1},
        headers={"Authorization": f"Bearer {test_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "patterns" in data
    assert "pattern_correlations" in data
    assert "context_analysis" in data
``` 