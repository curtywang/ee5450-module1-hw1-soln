import pytest
from fastapi.testclient import TestClient
from web_blackjack import app


@pytest.fixture
def base_client():
    return TestClient(app)


def test_home(base_client):
    response = base_client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Blackjack!"}


def test_create(base_client):
    response = base_client.get('/game/create/1')
    response_json = response.json()
    assert response.status_code == 201
    assert response_json['success'] is True
    assert len(response_json['game_id']) == 36
    assert len(response_json['termination_password']) == 36


if __name__ == '__main__':
    pytest.main()
