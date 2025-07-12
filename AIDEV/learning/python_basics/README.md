# Python Learning Path

## Cấu Trúc Thư Mục

```
python_basics/
├── 01_syntax/                 # Cú pháp cơ bản
│   ├── variables.py          # Biến và kiểu dữ liệu
│   ├── operators.py          # Toán tử và biểu thức
│   ├── control_flow.py       # Điều kiện và vòng lặp
│   ├── functions.py          # Hàm và module
│   └── file_handling.py      # Xử lý file cơ bản
│
├── 02_oop/                    # Lập trình hướng đối tượng
│   ├── classes.py            # Class và Object
│   ├── inheritance.py        # Kế thừa
│   ├── encapsulation.py      # Đóng gói
│   └── polymorphism.py       # Đa hình
│
├── 03_exceptions/            # Xử lý ngoại lệ
│   ├── try_except.py         # Try/Except/Finally
│   ├── custom_exceptions.py  # Custom Exceptions
│   ├── context_managers.py   # Context Managers
│   └── error_handling.py     # Error Handling Patterns
│
├── 04_async/                 # Lập trình bất đồng bộ
│   ├── async_basics.py       # Async/Await
│   ├── coroutines.py         # Coroutines
│   ├── event_loop.py         # Event Loop
│   └── async_io.py           # Async IO
│
├── 05_testing/               # Testing
│   ├── unittest_basics.py    # Unit Testing
│   ├── pytest_basics.py      # Pytest
│   ├── test_fixtures.py      # Test Fixtures
│   ├── mocking.py            # Mocking
│   └── test_coverage.py      # Test Coverage
│
├── 06_documentation/         # Documentation
│   ├── docstrings.py         # Docstrings
│   ├── type_hints.py         # Type Hints
│   ├── examples.py           # Examples
│   └── api_docs.py           # API Documentation
│
├── 07_packaging/             # Packaging
│   ├── package_structure.py  # Package Structure
│   ├── setup_py.py           # setup.py
│   ├── requirements_txt.py   # requirements.txt
│   └── distribution.py       # Distribution
│
├── 08_deployment/            # Deployment
│   ├── docker_basics.py      # Docker
│   ├── kubernetes_basics.py  # Kubernetes
│   ├── ci_cd.py              # CI/CD
│   └── web_servers.py        # Web Servers
│
├── 09_performance/           # Performance
│   ├── profiling.py          # Profiling
│   ├── memory_management.py  # Memory Management
│   ├── optimization.py       # Optimization
│   └── caching.py            # Caching
│
├── 10_debugging/             # Debugging
│   ├── debugger.py           # Debugger
│   ├── logging.py            # Logging
│   ├── stack_traces.py       # Stack Traces
│   └── debug_tools.py        # Debug Tools
│
├── 11_security/              # Security
│   ├── authentication.py     # Authentication
│   ├── password_hashing.py   # Password Hashing
│   ├── input_validation.py   # Input Validation
│   └── security_tools.py     # Security Tools
│
├── 12_database/              # Database
│   ├── sqlalchemy_basics.py  # SQLAlchemy
│   ├── migrations.py         # Migrations
│   ├── transactions.py       # Transactions
│   └── connection_pool.py    # Connection Pool
│
├── 13_api/                   # API Development
│   ├── fastapi_basics.py     # FastAPI
│   ├── restful_apis.py       # RESTful APIs
│   ├── authentication.py     # Authentication
│   └── validation.py         # Validation
│
├── 14_monitoring/            # Monitoring
│   ├── logging.py            # Logging
│   ├── metrics.py            # Metrics
│   ├── tracing.py            # Tracing
│   └── health_checks.py      # Health Checks
│
├── 15_concurrency/           # Concurrency
│   ├── threading.py          # Threading
│   ├── multiprocessing.py    # Multiprocessing
│   ├── async_io.py           # Async IO
│   └── queues.py             # Queues
│
└── 16_networking/            # Networking
    ├── tcp_ip.py             # TCP/IP
    ├── http.py               # HTTP
    ├── websockets.py         # WebSockets
    └── client_server.py      # Client/Server
```

## Yêu Cầu Hệ Thống

1. Python 3.10 trở lên
2. pip (Python package manager)
3. Virtual environment
4. Git

## Cài Đặt

1. Clone repository:
```bash
git clone <repository-url>
cd python_basics
```

2. Tạo môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

## Cách Sử Dụng

1. Mỗi thư mục chứa các bài tập và ví dụ cho một kỹ năng cụ thể
2. Đọc README.md trong mỗi thư mục để biết thêm chi tiết
3. Làm theo thứ tự từ 01 đến 16
4. Mỗi bài tập đều có:
   - Lý thuyết
   - Ví dụ
   - Bài tập thực hành
   - Giải pháp

## Tài Nguyên Bổ Sung

1. Sách:
   - "Python Crash Course"
   - "Learning Python"
   - "Fluent Python"

2. Khóa học online:
   - Python for Everybody (Coursera)
   - Python Programming (Udemy)
   - Real Python Tutorials

3. Tài liệu chính thức:
   - [Python Documentation](https://docs.python.org/3/)
   - [Pytest Documentation](https://docs.pytest.org/)
   - [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Đánh Giá

1. Bài tập hàng tuần
2. Project cuối mỗi module
3. Code review
4. Quiz kiến thức
5. Final project 