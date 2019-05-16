from typing import List, AnyStr

from dmsapi import config
from dmsapi.api.base import BaseAPI, require_auth


class Info(BaseAPI):
    @require_auth
    def _get_point(self):
        return self.session.get(config.entrypoints['POINT']).json()

    @require_auth
    def _get_basic(self):
        return self.session.get(config.entrypoints['BASIC']).json()

    @property
    def bad_point(self) -> int:
        return self._get_basic().get('goodPoint', -1)

    @property
    def good_point(self) -> int:
        return self._get_basic().get('badPoint', -1)

    @property
    def point_history(self) -> List:
        return self._get_point().get('point_history', [])

    @property
    def name(self) -> AnyStr:
        return self._get_basic().get('name', 'name')

    @property
    def number(self) -> int:
        return self._get_basic().get('number', -1)

    def penalty_level(self) -> int:
        return self._get_basic().get('penaltyLevel', -1)

    def penalty_status(self) -> bool:
        return self._get_basic().get('penaltyStatus', False)

