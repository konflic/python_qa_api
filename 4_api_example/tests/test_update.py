import random
import cerberus
import requests

# WARNING Bad Example: (Never use sensitive data like this!)
# See: https://www.youtube.com/watch?v=L9-I4NibguY
AUTH_DATA = {"login": "admin", "password": "admin"}


def test_create_add_get(base_url):
    response = requests.get(base_url + "/update/add")
    assert response.status_code == 405
    assert response.json().get("status") == "error"
    assert response.json().get("description") == "this method should not be here"


def test_create_add_post_auth(base_url):
    response = requests.post(base_url + "/update/add")
    assert response.status_code == 403
    assert response.json().get("status") == "error"
    assert response.json().get("description") == "authorization_required"


def test_authorization(base_url):
    response = requests.request("login", base_url + "/auth/login", json=AUTH_DATA)
    assert response.json().get("status") == "authorized"


schema = {
    "name": {"type": "string", "required": True},
    "surname": {"type": "string", "required": True},
    "grade": {"type": "number", "required": True},
    "sex": {"type": "string", "required": True}
}


def test_update_add_authorized_session(base_url):
    # Create session
    session = requests.Session()

    # Authorization
    session.request("login", base_url + "/auth/login", json=AUTH_DATA)

    # Create user
    data_to_make = {"name": "Test" + str(random.randint(10, 1000)), "surname": "TestSurname", "grade": 10, "sex": "male"}
    response = session.post(base_url + "/update/add", json=data_to_make)

    # Verify addition and response
    try:
        assert response.json().get("status") == "ok"
    except AssertionError:
        raise AssertionError(response.json())

    data = response.json().get("data")
    v = cerberus.Validator()
    assert v.validate(data, schema)
