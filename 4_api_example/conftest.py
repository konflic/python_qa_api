import pytest

from APIClient import APIClient


def pytest_addoption(parser):
    parser.addoption("--url", help="Url for test api location")


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
