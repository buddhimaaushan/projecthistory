def test_create_project(client):
    response = client.post("/api/projects", json={"name": "tempus", "colour": "#112233"})
    assert response.status_code == 201
    assert response.json()["name"] == "tempus"


def test_archive_project(client):
    created = client.post("/api/projects", json={"name": "old"}).json()
    archived = client.post("/api/projects/%d/archive" % created["id"])
    assert archived.json()["archived"] is True
    assert client.get("/api/projects").json() == []


def test_invalid_colour_is_rejected(client):
    response = client.post("/api/projects", json={"name": "bad", "colour": "purple"})
    assert response.status_code == 422


def test_rename_project(client):
    created = client.post("/api/projects", json={"name": "old"}).json()
    response = client.patch("/api/projects/%d" % created["id"], json={"name": "new"})
    assert response.status_code == 200
    assert response.json()["name"] == "new"
