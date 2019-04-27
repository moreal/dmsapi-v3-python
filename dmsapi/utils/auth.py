import base64
import hashlib

from typing import AnyStr


def make_user_data(user_agent: AnyStr, x_date: AnyStr) -> AnyStr:
    user_data = hashlib.sha3_512(base64.b64encode((user_agent + x_date).encode())).digest().hex()
    return user_data
