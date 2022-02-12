""" conftest setup"""

import pytest


@pytest.fixture()
def icao():
    return "KSSC"