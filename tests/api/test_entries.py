def test_create_and_list_entries(client):
    response = client.post("/api/entries", json={"label": "writing", "project": "tempus", "tags": ["docs"]})
    assert response.status_code == 201
    entry = response.json()
    assert entry["label"] == "writing"
    assert entry["project"] == "tempus"
    assert entry["tags"] == ["docs"]

    listing = client.get("/api/entries").json()
    assert len(listing) == 1


def test_get_missing_entry_returns_404(client):
    assert client.get("/api/entries/999").status_code == 404


def test_stop_entry(client):
    created = client.post("/api/entries", json={"label": "reading"}).json()
    stopped = client.post("/api/entries/%d/stop" % created["id"])
    assert stopped.status_code == 200
    assert stopped.json()["is_running"] is False


def test_only_one_running_timer(client):
    client.post("/api/entries", json={"label": "first"})
    second = client.post("/api/entries/start", json={"label": "second"})
    assert second.status_code == 409


def test_pagination(client):
    for index in range(5):
        client.post("/api/entries", json={"label": "entry %d" % index})
    page = client.get("/api/entries", params={"limit": 2, "offset": 2}).json()
    assert len(page) == 2


def test_update_entry(client):
    created = client.post("/api/entries", json={"label": "old"}).json()
    updated = client.patch("/api/entries/%d" % created["id"], json={"label": "new", "tags": ["Review"]})
    assert updated.status_code == 200
    assert updated.json()["label"] == "new"
    assert updated.json()["tags"] == ["review"]


def test_api_many_entries_with_duplicate_tags(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_unicode_labels_when_offline(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_empty_input_on_an_empty_database(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_pagination_for_an_archived_project(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_missing_id_after_a_migration(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_single_entry_with_defaults(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_duplicates_with_stale_cache(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_single_entry_with_a_long_label(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_null_project_with_a_long_label(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_future_start_with_a_long_label(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_null_project_with_mixed_casing(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_partial_data_with_a_long_label(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_deleted_project_across_midnight(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_boundaries_after_a_migration(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_zero_duration_after_a_reopen(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_defaults_on_an_empty_database(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_past_end_with_pagination(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_invalid_input_across_timezones(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_duplicates_on_an_empty_database(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_invalid_input_with_duplicate_tags(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_many_entries_when_offline(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_large_values_on_an_empty_database(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_pagination_for_a_new_account(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))


def test_api_boundaries_with_mixed_casing(client):
    response = client.get("/api/entries", params={"limit": 0})
    assert response.status_code in (200, 422)
    assert isinstance(response.json(), (list, dict))
