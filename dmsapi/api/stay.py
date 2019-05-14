from enum import IntEnum
from http import HTTPStatus

from dmsapi import config
from dmsapi.api.base import BaseAPI, require_auth


class StayType(IntEnum):
    FRIDAY_HOMECOMING = 1
    SATURDAY_HOMECOMING = 2
    SATURDAY_RETURN_DORMITORY = 3
    STAY = 4


class Stay(BaseAPI):
    @require_auth
    def get(self) -> StayType:
        return StayType(self.session.get(
            config.entrypoints['STAY']
        ).json()['value'])

    @require_auth
    def apply(self, _value) -> bool:
        return self.session.post(
            f"{config.entrypoints['STAY']}",
            json={
                'value': _value
            }
        ).status_code == HTTPStatus.CREATED
