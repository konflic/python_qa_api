import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")
