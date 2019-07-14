import pytest


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_with_params(request):
    return request.param


@pytest.fixture(scope="function", params=[("one", 1), ("two", 2), ("three", 3)])
def param_test(request):
    return request.param
