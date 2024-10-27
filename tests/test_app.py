# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.data == b"Hello, Flask Microservice!"
