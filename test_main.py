import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_legal_query_requires_input():
    response = client.post("/api/legal/ask", json={})
    assert response.status_code in [400, 422]
