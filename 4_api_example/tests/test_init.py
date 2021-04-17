import requests
import pytest


@pytest.mark.skip(reason="Нужно сначала аройти авторизацию")
def test_init_database(base_url):
    session = requests.Session()
    session.request("login", base_url + "/auth/login", json=AUTH_DATA)
    response = session.request("create", "{}/create/init".format(base_url))
    try:
        assert response.json().get("status") == "created"
    except AssertionError:
        raise AssertionError(response.json())


@pytest.mark.skip(reason="Нужно сначала аройти авторизацию")
def test_reinit_database(base_url):
    response = requests.request("{}/create/reinit".format(base_url))
    try:
        assert response.json().get("status") == "table dropped and created"
    except AssertionError:
        raise AssertionError(response.json())
