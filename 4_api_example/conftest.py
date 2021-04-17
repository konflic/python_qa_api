import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://my-api-examaple.herokuapp.com/api", help="Url for test api location")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
