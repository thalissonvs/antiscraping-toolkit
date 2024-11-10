import pytest
from fastapi.testclient import TestClient
from examples.api_block_userag import app, request_counter, REQUEST_LIMIT

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_request_counter():
    """Fixture que reseta o request_counter antes de cada teste."""
    request_counter.clear()

def test_access_not_blocked_initially():
    """Teste para garantir que o primeiro acesso não está bloqueado."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome! You are not blocked."}

def test_block_after_too_many_requests():
    """Teste para garantir que o acesso é bloqueado após muitas requisições."""
    for _ in range(REQUEST_LIMIT):
        response = client.get("/")
        assert response.status_code == 200  # Ainda não bloqueado

    # No próximo acesso, deve ser bloqueado
    response = client.get("/")
    assert response.status_code == 429
    assert response.json() == {"detail": "Too many requests. You are temporarily blocked."}

def test_different_user_agent_resets_block():
    """Teste para garantir que mudar o User-Agent evita o bloqueio."""
    headers = {"User-Agent": "TestAgent"}
    for _ in range(REQUEST_LIMIT):
        response = client.get("/", headers=headers)
        assert response.status_code == 200

    # Bloqueado com o User-Agent atual
    response = client.get("/", headers=headers)
    assert response.status_code == 429

    # Mudando o User-Agent, deve estar liberado
    headers = {"User-Agent": "AnotherAgent"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
