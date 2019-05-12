from typing import Callable, Any

from dmsapi.core.session import DMSAccountSession


def require_auth(func: Callable[..., Any], *args):
    def wrap():
        self: BaseAPI = args[0]
        session = self.session
        if session.is_authenticated:
            func(*args)

    return wrap


class BaseAPI:
    """
    Base class for DMS API
    """

    def __init__(self, _session: DMSAccountSession):
        self._session = _session

    def apply(self):
        pass

    def get(self):
        pass

    @property
    def session(self):
        return self._session
