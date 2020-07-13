import random
import cerberus


def test_create_add_get(api_client):
    response = api_client.get("/update/add")
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["description"] == "method_not_allowed"


def test_create_add_post_auth(api_client):
    response = api_client.post("/update/add")
    assert response.status_code == 403
    assert response.json()["status"] == "error"
    assert response.json()["description"] == "authorization_required"


def test_authorization(api_client):
    data = {"user": "admin", "password": "12345678"}
    response = api_client.custom("login", "/auth/login", json=data)
    assert response.json()["status"] == "ok"


schema = {
    "name": {"type": "string", "required": True},
    "surname": {"type": "string", "required": True},
    "grade": {"type": "number", "required": True}
}


def test_update_add_authorized_session(api_client):
    # Создание сессии
    session = api_client.create_session()
    # Авторизация
    data = {"user": "admin", "password": "12345678"}
    session.request("login", api_client.base_address + "/auth/login", json=data)
    # Создание пользователя
    data_to_make = {"name": "Test" + str(random.randint(10, 1000)), "surname": "TestSurname", "grade": 10}
    response = session.post(api_client.base_address + "/update/add", json=data_to_make)
    # Проверяем что добавление отработало
    assert response.json()["status"] == "ok"
    data = response.json()["data"]
    v = cerberus.Validator()
    assert v.validate(data, schema)
