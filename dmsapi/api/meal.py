from dmsapi.core.session import DMSAccountSession


class Meal:
    def __init__(self, _session: DMSAccountSession):
        self._session = _session
