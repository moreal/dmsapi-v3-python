from json import JSONDecodeError

from dmsapi import config
from dmsapi.api.base import BaseAPI, require_auth


class Extension(BaseAPI):
    @require_auth
    def get(self, _time):
        return self.session.get(
            f"{config.entrypoints['EXTENSION']}/{_time}"
        ).json()

    @require_auth
    def apply(self, _time: int, _class: int, _seat: int) -> bool:
        return self.session.post(
            f"{config.entrypoints['EXTENSION']}/{_time}",
            json={
                'classNum': _class,
                'seatNum': _seat
            }
        ).status_code == 200

    def map(self, _time: int, _room: int):
        return self.session.get(
            f"{config.entrypoints['EXTENSION']}/map/{_time}/{_room}"
        ).json()
