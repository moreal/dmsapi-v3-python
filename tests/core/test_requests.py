from dmsapi.core import requests


def test_can_access_methods():
    requests.get
    requests.post
    requests.patch
    requests.put
    requests.delete
    requests.request
    requests.options
