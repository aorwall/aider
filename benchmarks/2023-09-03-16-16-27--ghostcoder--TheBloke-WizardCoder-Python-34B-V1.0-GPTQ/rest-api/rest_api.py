import requests
from typing import Dict

class RestAPI:
    BASE_URL = 'http://localhost:50000/'

    def __init__(self, database=None):
        if database is None:
            self._database = {}
        else:
            self._database = database

    def _request(self, method: str, endpoint: str, data: Dict[str, int] = None) -> Dict[str, int]:
        response = getattr(requests, method)(self.BASE_URL + endpoint, json=data)
        return response.json()

    def get(self, url: str, payload: Dict[str, int] = None) -> Dict[str, int]:
        return self._request('get', url, payload)

    def post(self, url: str, payload: Dict[str, int] = None) -> Dict[str, int]:
        return self._request('post', url, payload)
