import datetime

from requests import Session, Response

from dmsapi import config
from dmsapi.api.extension import Extension
from dmsapi.api.goingout import Goingout
from dmsapi.api.info import Info
from dmsapi.api.meal import Meal
from dmsapi.api.music import Music
from dmsapi.api.stay import Stay

from dmsapi.core.auth import ApiCallAuth


class DMSSession(Session):
    def __init__(self, _id=None, _password=None, _timezone: datetime.timezone = None):
        super().__init__()

        if _timezone is None:
            _timezone = datetime.timezone(datetime.timedelta(hours=9))

        self._api_call_auth_instance = ApiCallAuth(_timezone)

        self._id = _id
        self._password = _password

        self.access_token = None
        self.refresh_token = None

        self._is_authenticated = False

    def authenticate(self):
        response: Response = self.post(config.entrypoints['AUTH'], json={
            'id': self._id,
            'password': self._password
        })

        self.access_token = response.json().get('accessToken', None)
        self.refresh_token = response.json().get('refreshToken', None)

        self._is_authenticated = (response.status_code == 200)

    @property
    def is_authenticated(self) -> bool:
        return self._is_authenticated

    def request(self, method, url, **kwargs):
        if self.access_token is not None:
            kwargs.setdefault('headers', dict())
            kwargs['headers'].update({
                'Authorization': 'Bearer ' + self.access_token
            })

        return super().request(
            method,
            url,
            auth=self._api_call_auth_instance,
            **kwargs)

    @property
    def extension(self) -> Extension:
        return Extension(self)

    @property
    def goingout(self) -> Goingout:
        return Goingout(self)

    @property
    def info(self) -> Info:
        return Info(self)

    @property
    def meal(self) -> Meal:
        return Meal(self)

    @property
    def music(self) -> Music:
        return Music(self)

    @property
    def stay(self) -> Stay:
        return Stay(self)
