""" basic main testing routes"""

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_main():
    """test root entry for basic return and 200"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b'"hello world"'

def test_read_input_route(icao):
    """test with fixture user input"""
    response = client.get("/taf/"+icao)
    assert response.status_code == 200

# work on mock patch to fake results
def test_class_implement_route(mock_function,test_data):
    """test retrieve route w class"""
    mock_function.return_value = test_data
    response = client.get('/test')
    assert response.status_code == 200
    assert response.content == b'{"id":1,"userId":1}'
