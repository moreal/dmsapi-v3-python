from http import HTTPStatus
from typing import AnyStr

from dmsapi import config
from dmsapi.api.base import BaseAPI, require_auth


class Goingout(BaseAPI):
    @require_auth
    def get(self):
        return self.session.get(
            config.entrypoints['GOINGOUT']
        ).json()

    @require_auth
    def apply(self, _date: AnyStr, _reason: AnyStr) -> bool:
        """
        :param _date: format '05-17 02:30 ~ 05:30'
        :param _reason: the reason to go out
        :return: bool of success
        """

        return self.session.post(
            f"{config.entrypoints['GOINGOUT']}",
            json={
                'date': _date,
                'reason': _reason
            }
        ).status_code == HTTPStatus.CREATED

    @require_auth
    def delete(self, _apply_id: int):
        """
        :param _apply_id: applyId of goingout
        :return: bool of success
        """
        return 200 == self.session.delete(
            config.entrypoints['GOINGOUT'],
            json={
                'applyId': _apply_id
            }
        ).status_code

    @require_auth
    def update(self, _apply_id: int, _date: AnyStr, _reason) -> bool:
        """
        :param _apply_id: applyId of goingout
        :param _date: format '05-17 02:30 ~ 05:30'
        :param _reason: the reason to go out
        :return: bool of success
        """
        return 201 == self.session.patch(
            config.entrypoints['GOINGOUT'],
            json={
                'applyId': _apply_id,
                'date': _date,
                'reason': _reason
            }
        ).status_code
