from dmsapi import config
from dmsapi.core import requests
from requests import Request
from dmsapi.utils.auth import make_user_data

ROOT_PATH = config.entrypoints['ROOT']


def dms_check_user_data_process(request: Request, context):
    user_agent = request.headers.get('User-Agent', None)
    x_date = request.headers.get('X-Date', None)
    user_data = request.headers.get('User-Data', None)

    if user_agent is None or x_date is None or user_data is None or user_data != make_user_data(user_agent, x_date):
        context.status_code = 418
        return "I'm a teapot"
    else:
        context.status_code = 404
        return 'Not Found'


def test_request_with_auth(requests_mock):
    requests_mock.get(ROOT_PATH, text=dms_check_user_data_process)
    resp = requests.get(ROOT_PATH)

    assert 418 != resp.status_code
