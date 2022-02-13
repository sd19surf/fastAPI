""" basic main testing routes"""


from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app.main import app
from app.main import retrieve

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b'"hello world"'

def test_read_input_route(icao):
    """test with fixture user input"""
    response = client.get("/taf/{icao}")
    assert response.status_code == 200

# work on mock patch to fake results
def test_class_implement_route(test_data):
    """test retrieve route w class"""
    response = client.get('/test')
    assert response.status_code == 200
