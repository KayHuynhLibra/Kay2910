import logging
from datetime import datetime
from typing import Dict, Any
import sentry_sdk
from prometheus_client import Counter, Histogram, start_http_server
from elasticsearch import Elasticsearch

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Initialize Sentry for error tracking
sentry_sdk.init(
    dsn="your-sentry-dsn",  # Replace with your Sentry DSN
    traces_sample_rate=1.0,
)

# Initialize Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Prometheus metrics
REQUEST_COUNT = Counter(
    'request_count', 'Total number of requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency in seconds',
    ['method', 'endpoint']
)

class Monitoring:
    @staticmethod
    def log_request(method: str, endpoint: str, status: int, latency: float):
        """Log request details to Elasticsearch"""
        doc = {
            'timestamp': datetime.utcnow(),
            'method': method,
            'endpoint': endpoint,
            'status': status,
            'latency': latency
        }
        es.index(index='api-logs', body=doc)
        
        # Update Prometheus metrics
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=status).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)

    @staticmethod
    def log_error(error: Exception, context: Dict[str, Any] = None):
        """Log error details to Sentry and Elasticsearch"""
        sentry_sdk.capture_exception(error)
        
        error_doc = {
            'timestamp': datetime.utcnow(),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'context': context or {}
        }
        es.index(index='error-logs', body=error_doc)
        logger.error(f"Error occurred: {str(error)}", exc_info=True)

    @staticmethod
    def log_metric(name: str, value: float, tags: Dict[str, str] = None):
        """Log custom metrics"""
        metric_doc = {
            'timestamp': datetime.utcnow(),
            'metric_name': name,
            'value': value,
            'tags': tags or {}
        }
        es.index(index='metrics', body=metric_doc)

# Start Prometheus metrics server
start_http_server(8000) 