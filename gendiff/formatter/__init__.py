from .stylish import make_stylish
from .plain import make_plain
from .json import make_json


def formated(data, format):
    if format == 'stylish':
        return make_stylish(data)
    elif format == 'plain':
        return make_plain(data)
    elif format == 'json':
        return make_json(data)
    else:
        raise ValueError((f'format {format} not supported'))
