from dmsapi.core.session import DMSAccountSession


class BaseAPI:
    """
    Base class for DMS API
    """

    def __init__(self, _session: DMSAccountSession):
        self._session = _session
