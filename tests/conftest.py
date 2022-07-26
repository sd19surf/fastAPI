""" conftest setup"""

import pytest
from requests import session

@pytest.fixture
def mock_env_user_local(monkeypatch):
    monkeypatch.setenv("SOLARLUNAR_ENV", "local")

@pytest.fixture
def mock_env_user_prod(monkeypatch):
    monkeypatch.setenv("SOLARLUNAR_ENV", "production")
