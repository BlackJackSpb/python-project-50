from .stylish import make_stylish
from .plain import make_plain
from .json import make_json


def formated(data, format='stylich'):
    if format == 'plain':
        return make_plain(data)
    if format == 'json':
        return make_json(data)
    return make_stylish(data)
