from .stylish import make_stylish


def formated(data, format='stylich'):
    if format == 'stylish':
        return make_stylish(data)