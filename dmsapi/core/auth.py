import time

from requests import Request
from requests.auth import AuthBase

from dmsapi.utils.auth import make_user_data


class ApiCallAuth(AuthBase):
    def __call__(self, request: Request):
        user_agent = 'My Agent'
        x_date = time.strftime("%a %b %d %Y %H:%M:%S")

        request.headers['User-Agent'] = user_agent
        request.headers['X-Date'] = x_date
        request.headers['User-Data'] = make_user_data(user_agent, x_date)

        return request
