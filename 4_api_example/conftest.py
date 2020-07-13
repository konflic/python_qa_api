import pytest
import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def create_session(self):
        return requests.Session()

    def custom(self, method, path="/", **kwargs):
        url = self.base_address + path
        return requests.request(method, url=url, **kwargs)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption("--url", default="http://localhost:8888")


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
