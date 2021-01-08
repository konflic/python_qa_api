import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(url, code, method):
    target = url + f"/status/{code}"
    response = method(url=target)
    assert response.status_code == code
