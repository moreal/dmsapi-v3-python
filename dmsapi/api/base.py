from json import JSONDecodeError
from typing import Callable, Any


def require_auth(func: Callable[..., Any], *args):
    def wrap(*args) -> dict:
        self: BaseAPI = args[0]
        session = self.session
        if not session.is_authenticated:
            session.authenticate()

        try:
            return func(*args)
        except JSONDecodeError:
            return {}

    return wrap


class BaseAPI:
    """
    Base class for DMS API
    """

    def __init__(self, _session):
        self._session = _session

    def apply(self):
        pass

    def get(self):
        pass

    @property
    def session(self):
        return self._session
