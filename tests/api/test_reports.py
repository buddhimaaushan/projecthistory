def test_summary_empty(client):
    body = client.get("/api/reports/summary").json()
    assert body["entries"] == 0
    assert body["total_seconds"] == 0
    assert body["by_project"] == {}


def test_summary_groups_by_project(client):
    client.post("/api/entries", json={"label": "a", "project": "tempus", "tags": []})
    client.post("/api/entries", json={"label": "b"})
    body = client.get("/api/reports/summary").json()
    assert body["entries"] == 2
    assert "tempus" in body["by_project"]
    assert "unassigned" in body["by_project"]


def test_csv_export_has_a_header_row(client):
    client.post("/api/entries", json={"label": "writing"})
    response = client.get("/api/reports/export.csv")
    assert response.status_code == 200
    assert response.text.splitlines()[0] == "label,project,start,end,seconds"
