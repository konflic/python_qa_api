"""Пример на jsonschema"""
import cerberus


def test_api_json_schema(api_client):
    """
    Проверка структуры ответа за запрос /todos/1
    """
    res = api_client.get(path="/todos/1")

    schema = {
            "id": {"type": "number"},
            "userId": {"type": "number"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
