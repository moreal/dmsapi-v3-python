from dmsapi import config
from dmsapi.api.base import BaseAPI, require_auth


class Extension(BaseAPI):
    @require_auth
    def get(self):
        self.session.get(config.entrypoints['EXTENSION'])

