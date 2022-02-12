""" basic main testing routes"""


from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app.main import app
from app.main import retrieve

client = TestClient(app)

def test_read_main():
    """test basic route return"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b'"hello world"'

def test_read_input_route(icao):
    """test with fixture user input"""
    response = client.get("/taf/{icao}")
    assert response.status_code == 200

@patch('app.retrieve.Retrieve.get_data')
def test_getting_data_when_response_is_ok(mock_get):
    """test with mock external api"""
    test_data = [{
        'userId': 1,
        'id': 1
    }]
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = test_data
    response = retrieve.Retrieve().data
    assert response.json() == test_data