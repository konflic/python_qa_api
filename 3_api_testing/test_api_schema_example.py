from jsonschema import validate


def test_api_json_schema(api_client):
    """Проверка структуры ответа за запрос /todos/1"""
    res = api_client.get(path="/todos/1")

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "userId": {"type": "number"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        },
        "required": ["id", "userId", "title", "completed"]
    }

    validate(instance=res.json(), schema=schema)
