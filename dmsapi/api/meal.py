from typing import AnyStr

from dmsapi import config
from dmsapi.api.base import BaseAPI


class Meal(BaseAPI):
    def get(self, _date: AnyStr):
        return self.session.get(
            f"{config.entrypoints['MEAL']}/{_date}"
        ).json()
