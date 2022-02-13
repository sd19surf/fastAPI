""" conftest setup"""

import pytest
from unittest.mock import Mock, patch
from app import retrieve


@pytest.fixture()
def icao():
    return "KSSC"

@pytest.fixture(scope="session",autouse=True)
def test_data():
    data = [{
    'id': 1,
    'userId': 1
    }]
    return data

@pytest.fixture(scope="session", autouse=True)
@patch('app.retrieve.Retrieve.get_data')
def test_getting_data_when_response_is_ok(mock_get,test_data):
    """"""
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = test_data
    response = retrieve.Retrieve().get_data()
    return response