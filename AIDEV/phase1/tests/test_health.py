from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "version" in response.json()
    assert "debug" in response.json()

def test_metrics():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    # Metrics should be in Prometheus format
    assert "http_requests_total" in response.text
    assert "http_request_duration_seconds" in response.text 