from prometheus_client import Counter, Histogram, Gauge, Summary
import time
from functools import wraps

# Request metrics
REQUEST_COUNT = Counter(
    'request_count',
    'Total number of requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'request_latency_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

# Chat metrics
CHAT_MESSAGE_COUNT = Counter(
    'chat_message_count',
    'Total number of chat messages processed',
    ['agent_id']
)

CHAT_RESPONSE_TIME = Histogram(
    'chat_response_time_seconds',
    'Chat response time in seconds',
    ['agent_id']
)

# Learning metrics
MODEL_TRAINING_COUNT = Counter(
    'model_training_count',
    'Total number of model training sessions',
    ['model_name']
)

MODEL_TRAINING_TIME = Histogram(
    'model_training_time_seconds',
    'Model training time in seconds',
    ['model_name']
)

MODEL_EVALUATION_SCORE = Gauge(
    'model_evaluation_score',
    'Model evaluation score',
    ['model_name', 'metric']
)

# Data metrics
DATASET_SIZE = Gauge(
    'dataset_size',
    'Size of datasets in bytes',
    ['dataset_name']
)

DATASET_VERSION_COUNT = Gauge(
    'dataset_version_count',
    'Number of versions per dataset',
    ['dataset_name']
)

# System metrics
MEMORY_USAGE = Gauge(
    'memory_usage_bytes',
    'Memory usage in bytes',
    ['component']
)

CPU_USAGE = Gauge(
    'cpu_usage_percent',
    'CPU usage percentage',
    ['component']
)

# Error metrics
ERROR_COUNT = Counter(
    'error_count',
    'Total number of errors',
    ['component', 'error_type']
)

def track_request_metrics(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = await func(*args, **kwargs)
            status = 'success'
        except Exception as e:
            status = 'error'
            raise e
        finally:
            duration = time.time() - start_time
            REQUEST_COUNT.labels(
                method=func.__name__,
                endpoint=func.__name__,
                status=status
            ).inc()
            REQUEST_LATENCY.labels(
                method=func.__name__,
                endpoint=func.__name__
            ).observe(duration)
        return response
    return wrapper

def track_chat_metrics(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = await func(*args, **kwargs)
            CHAT_MESSAGE_COUNT.labels(agent_id=args[0].agent_id).inc()
            CHAT_RESPONSE_TIME.labels(agent_id=args[0].agent_id).observe(
                time.time() - start_time
            )
            return response
        except Exception as e:
            ERROR_COUNT.labels(
                component='chat',
                error_type=type(e).__name__
            ).inc()
            raise e
    return wrapper

def track_learning_metrics(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = await func(*args, **kwargs)
            model_name = kwargs.get('model_name', 'unknown')
            MODEL_TRAINING_COUNT.labels(model_name=model_name).inc()
            MODEL_TRAINING_TIME.labels(model_name=model_name).observe(
                time.time() - start_time
            )
            return response
        except Exception as e:
            ERROR_COUNT.labels(
                component='learning',
                error_type=type(e).__name__
            ).inc()
            raise e
    return wrapper

def update_system_metrics():
    """Update system metrics periodically"""
    import psutil
    process = psutil.Process()
    
    # Update memory usage
    MEMORY_USAGE.labels(component='total').set(process.memory_info().rss)
    MEMORY_USAGE.labels(component='heap').set(process.memory_info().heap)
    
    # Update CPU usage
    CPU_USAGE.labels(component='process').set(process.cpu_percent())
    CPU_USAGE.labels(component='system').set(psutil.cpu_percent()) 