def test_init_database(api_client):
    response = api_client.get("/create/init")
    try:
        assert response.json().get("status") == "created"
    except AssertionError:
        raise AssertionError(response.json())

def test_reinit_database(api_client):
    response = api_client.get("/create/reinit")
    try:
        assert response.json().get("status") == "table dropped and created"
    except AssertionError:
        raise AssertionError(response.json())