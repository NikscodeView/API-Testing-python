import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, headers=None):
        return requests.get(f"{self.base_url}{path}", headers=headers)

    def post(self, path, json=None, headers=None):
        return requests.post(f"{self.base_url}{path}", json=json, headers=headers)

    def delete(self, path, headers=None):
        return requests.delete(f"{self.base_url}{path}", headers=headers)

