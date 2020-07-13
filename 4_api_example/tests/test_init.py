def test_init_database(api_client):
    response = api_client.get("/create/init")
    assert response.json().get("status") == "created"


def test_reinit_database(api_client):
    response = api_client.get("/create/reinit")
    assert response.json().get("status") == "table dropped and created"
