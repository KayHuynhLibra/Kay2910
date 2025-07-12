"""
Bài tập 12: Monitoring

Mục tiêu:
- Hiểu cách thiết lập monitoring
- Thực hành với Prometheus và Grafana
- Sử dụng logging và tracing
"""

import logging
from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# TODO: Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# TODO: Prometheus metrics
# Counter cho số lượng request
REQUEST_COUNT = Counter(
    'request_count',
    'Number of requests',
    ['method', 'endpoint', 'status']
)

# Histogram cho thời gian xử lý
REQUEST_LATENCY = Histogram(
    'request_latency_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

# Gauge cho số lượng active users
ACTIVE_USERS = Gauge(
    'active_users',
    'Number of active users'
)

# TODO: OpenTelemetry tracing
def setup_tracing():
    """
    Cấu hình tracing với OpenTelemetry
    """
    trace.set_tracer_provider(TracerProvider())
    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",
        agent_port=6831,
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)
    return trace.get_tracer(__name__)

tracer = setup_tracing()

# TODO: Middleware cho monitoring
class MonitoringMiddleware:
    """
    Middleware để thu thập metrics
    """
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request, call_next):
        start_time = time.time()
        
        # Tăng counter cho request
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status="pending"
        ).inc()
        
        try:
            response = await call_next(request)
            
            # Cập nhật counter với status
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
                status=response.status_code
            ).inc()
            
            return response
        
        except Exception as e:
            # Cập nhật counter với error
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.url.path,
                status="error"
            ).inc()
            raise e
        
        finally:
            # Ghi lại latency
            REQUEST_LATENCY.labels(
                method=request.method,
                endpoint=request.url.path
            ).observe(time.time() - start_time)

# TODO: Health check endpoint
async def health_check():
    """
    Endpoint kiểm tra sức khỏe hệ thống
    """
    return {
        "status": "healthy",
        "timestamp": time.time()
    }

# TODO: Metrics endpoint
async def metrics():
    """
    Endpoint trả về metrics
    """
    return {
        "request_count": REQUEST_COUNT._value.get(),
        "active_users": ACTIVE_USERS._value.get()
    }

# TODO: Logging decorator
def log_execution_time(func):
    """
    Decorator để log thời gian thực thi
    """
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(
                f"Function {func.__name__} executed in {execution_time:.2f} seconds"
            )
            return result
        except Exception as e:
            logger.error(
                f"Error in {func.__name__}: {str(e)}",
                exc_info=True
            )
            raise
    return wrapper

# TODO: Tracing decorator
def trace_function(func):
    """
    Decorator để trace function
    """
    async def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__) as span:
            span.set_attribute("function.name", func.__name__)
            try:
                result = await func(*args, **kwargs)
                span.set_status(trace.Status(trace.StatusCode.OK))
                return result
            except Exception as e:
                span.set_status(trace.Status(trace.StatusCode.ERROR))
                span.record_exception(e)
                raise
    return wrapper

# TODO: Example usage
@log_execution_time
@trace_function
async def process_data(data):
    """
    Function xử lý dữ liệu với monitoring
    """
    # Giả lập xử lý
    time.sleep(1)
    return {"processed": True}

# TODO: Start Prometheus server
if __name__ == "__main__":
    start_http_server(8000)
    logger.info("Prometheus metrics server started on port 8000")

"""
Bài tập về nhà:
1. Tạo một hệ thống monitoring cho một ứng dụng FastAPI
2. Tạo một hệ thống monitoring cho một ứng dụng machine learning
3. Tạo một hệ thống monitoring cho một hệ thống microservices
4. Tạo một hệ thống monitoring cho một ứng dụng web với Nginx
5. Tạo một hệ thống monitoring cho một hệ thống database
""" 