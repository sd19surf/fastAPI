""" conftest setup"""

import pytest, pytest_mock
from unittest.mock import Mock, patch
from app import retrieve


@pytest.fixture()
def icao():
    return "KSSC"

@pytest.fixture(scope="session",autouse=True)
def test_data():
    data = {
    'id': 1,
    'userId': 1
    }
    return data

@pytest.fixture()
def mock_function(mocker):
    return mocker.patch("app.retrieve.Retrieve.get_data")

