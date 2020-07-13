import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def method(request):
    m = request.config.getoption("--method")
    if m == "post":
        return requests.post
    elif m == "get":
        return requests.get
    elif m == "delete":
        return requests.delete
    elif m == "put":
        return requests.put
    elif m == "patch":
        return requests.patch
