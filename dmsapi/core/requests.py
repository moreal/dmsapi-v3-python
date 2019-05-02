import requests

from typing import AnyStr, Callable, Any
from dmsapi.core.auth import ApiCallAuth

api_call_auth = ApiCallAuth()


def __getattr__(name: AnyStr) -> Callable[[AnyStr, Any], requests.Response]:
    def request(url, **kwargs) -> requests.Response:
        return getattr(requests, name)(url, auth=api_call_auth, **kwargs)

    return request
