""" conftest setup"""

import pytest


@pytest.fixture()
def icao():
    return "KSSC"

@pytest.fixture()
def test_data():
    data = [{
    'userId': 1,
    'id': 1
    }]
    return data