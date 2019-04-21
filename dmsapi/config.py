from typing import Dict, AnyStr
from configparser import ConfigParser


class Config:
    def __init__(self, path):
        self._config = ConfigParser()
        self._config.read(path)

    @property
    def entrypoints(self) -> Dict[AnyStr, AnyStr]:
        return self._config['ENTRYPOINTS']

