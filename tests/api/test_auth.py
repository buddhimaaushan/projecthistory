import pytest

from tests.api.conftest import USER


def test_register_and_login(anon_client):
    assert anon_client.post("/api/auth/register", json=USER).status_code == 201
    response = anon_client.post(
        "/api/auth/login", data={"username": USER["email"], "password": USER["password"]}
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"


def test_duplicate_email_is_rejected(anon_client):
    anon_client.post("/api/auth/register", json=USER)
    assert anon_client.post("/api/auth/register", json=USER).status_code == 409


def test_wrong_password(anon_client):
    anon_client.post("/api/auth/register", json=USER)
    response = anon_client.post(
        "/api/auth/login", data={"username": USER["email"], "password": "nope"}
    )
    assert response.status_code == 401


def test_me_requires_token(anon_client):
    assert anon_client.get("/api/auth/me").status_code == 401


@pytest.mark.parametrize("path", ["/api/entries", "/api/projects", "/api/reports/summary"])
def test_endpoints_require_token(anon_client, path):
    assert anon_client.get(path).status_code == 401
