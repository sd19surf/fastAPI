""" basic main testing routes"""

from fastapi.testclient import TestClient
import os
from app.main import app


client = TestClient(app)


def test_no_token(mock_env_user_local):
    response = client.get("/users/me")
    assert os.getenv('SOLARLUNAR_ENV') == 'local'
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "call logic to run in local env"}


def test_token(mock_env_user_prod):
    response = client.get("/users/me", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200, response.text
    assert response.json() == {"token": "testtoken"}


def test_incorrect_token(mock_env_user_prod):
    response = client.get("/users/me", headers={"Authorization": "Notexistent testtoken"})
    assert response.status_code == 200, response.text
    assert response.json() == {"token": None}
