import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 500])
def test_url_status(url, code, method):
    response = method(url + "/status/{}".format(code))
    assert response.status_code == code
