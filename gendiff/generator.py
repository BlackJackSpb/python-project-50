from .parser import parsers


def generate_diff(first_file, second_file):
    data1, data2 = parsers(first_file, second_file)
    diff = []

    def to_str(item):
        return str(item).lower()

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            diff.append(f'  - {key}: {to_str(data1[key])}')
        elif key not in data1:
            diff.append(f'  + {key}: {to_str(data2[key])}')
        elif key in data1 and data2 and data1[key] != data2[key]:
            diff.append(f'  - {key}: {to_str(data1[key])}')
            diff.append(f'  + {key}: {to_str(data2[key])}')
        else:
            diff.append(f'  {key}: {to_str(data1[key])}')

    to_str_diff = '\n'.join(diff)
    return f"{{\n{to_str_diff}\n}}"
