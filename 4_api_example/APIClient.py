import requests


class APIClient:
    """Simplified API Client for passed base_address"""

    def __init__(self, base_address):
        self.base_address = base_address
        self.session = None

    def create_session(self):
        if self.session is None:
            self.session = requests.Session()
        return self.session

    def custom(self, method, path="/", **kwargs):
        url = self.base_address + path
        return requests.request(method, url=url, **kwargs)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)
