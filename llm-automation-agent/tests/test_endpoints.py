import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_endpoint():
    response = client.post("/run", params={"task": "Format /data/format.md with prettier 3.4.2"})
    assert response.status_code == 200
    assert "status" in response.json()

def test_read_endpoint_valid():
    response = client.get("/read", params={"path": "/data/format.md"})
    assert response.status_code == 200

def test_read_endpoint_invalid_path():
    response = client.get("/read", params={"path": "../invalid.txt"})
    assert response.status_code == 400

def test_read_endpoint_not_found():
    response = client.get("/read", params={"path": "/data/nonexistent.txt"})
    assert response.status_code == 404
    #hello