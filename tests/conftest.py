""" conftest setup"""

import pytest


@pytest.fixture()
def icao():
    """defines icao variable for session use"""
    return "KSSC"

@pytest.fixture(scope="session",autouse=True)
def test_data():
    """defines test data for input for mock"""
    data = {
    'id': 1,
    'userId': 1
    }
    return data

@pytest.fixture()
def mock_function(mocker):
    """defines get_data mock function for api tests"""
    return mocker.patch("app.retrieve.Retrieve.get_data")
