from .stylish import make_stylish
from .plain import make_plain


def formated(data, format='stylich'):
    if format == 'plain':
        return make_plain(data)
    return make_stylish(data)
