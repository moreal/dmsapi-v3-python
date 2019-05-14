from requests import Session, Response

from dmsapi import config
from dmsapi.api.extension import Extension
from dmsapi.api.goingout import Goingout
from dmsapi.api.meal import Meal
from dmsapi.api.music import Music
from dmsapi.api.point import Point
from dmsapi.api.stay import Stay
from dmsapi.core.requests import api_call_auth


class DMSAccountSession(Session):
    def __init__(self, _id, _password):
        super().__init__()

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

        return super().request(method, url, auth=api_call_auth, **kwargs)

    @property
    def extension(self) -> Extension:
        return Extension(self)

    @property
    def goingout(self) -> Goingout:
        return Goingout(self)

    @property
    def point(self) -> Point:
        return Point(self)

    @property
    def meal(self) -> Meal:
        return Meal(self)

    @property
    def music(self) -> Music:
        return Music(self)

    @property
    def stay(self) -> Stay:
        return Stay(self)
