"""
retrieve class test
"""
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app import retrieve

def test_retrieve_init():
    """ Test the init of the retrieve class"""
    test_retrieve = retrieve.Retrieve()
    assert test_retrieve.config['test']['dev'] == "https://google.com"

@patch('app.retrieve.Retrieve.get_data')
def test_getting_data_when_response_is_ok(mock_get,test_data):
    """"""
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = test_data
    response = retrieve.Retrieve().get_data()
    assert response.json() == test_data