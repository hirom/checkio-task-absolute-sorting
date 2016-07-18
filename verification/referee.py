
cover = """def cover(func, data):
    result = func(tuple(data))
    if not isinstance(result, (list, tuple)):
        raise TypeError("The result should be a list or a tuple")
    return result
"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        function_name={
            "python": "checkio",
            "js": "absoluteSorting"
        }
    ).on_ready)
