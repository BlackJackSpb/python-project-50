from .parser import parsers
from .comparison import compare_data


def generate_diff(file_name1, file_name2, format_name='stylish'):
    data1 = parsers(file_name1)
    data2 = parsers(file_name2)
    diff = compare_data(data1, data2)
    return diff
