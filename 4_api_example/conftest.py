import pytest


def pytest_addoption(parser):
    parser.addoption("--url", help="Url for test api location", required=True)


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
