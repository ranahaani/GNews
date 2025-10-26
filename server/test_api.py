import pytest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)
API_KEY = "test-key"

# Test /news endpoint
def test_get_news():
    response = client.get("/news", params={"q": "AI", "limit": 2}, headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "results" in response.json()

# Test /trending endpoint
def test_get_trending():
    response = client.get("/trending", params={"country": "US", "limit": 2}, headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "results" in response.json()

# Test /topics/{topic} endpoint
def test_get_topic_news():
    response = client.get("/topics/TECHNOLOGY", params={"limit": 2}, headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "results" in response.json()

# Test /locations/{location} endpoint
def test_get_location_news():
    response = client.get("/locations/New York", params={"limit": 2}, headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "results" in response.json()

# Test /auth/register endpoint
def test_register():
    response = client.post("/auth/register")
    assert response.status_code == 200
    assert "api_key" in response.json()

# Test authentication failure
def test_auth_fail():
    response = client.get("/news", params={"q": "AI"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"

# Test rate limiting (simulate by calling many times)
def test_rate_limit():
    for _ in range(101):
        response = client.get("/news", params={"q": "AI"}, headers={"X-API-Key": API_KEY})
    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded"
