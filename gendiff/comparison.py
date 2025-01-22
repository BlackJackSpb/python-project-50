
def compare_data(data1, data2):
    return {
        'name': 'main',
        'type': 'root',
        'children': adding_comparisons(data1, data2)
    }


def add(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'add'
    }


def remove(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'remove'
    }


def inside(key, value1, value2):
    return {
        'name': key,
        'type': 'inside',
        'children': adding_comparisons(value1, value2)
    }


def modified(key, value1, value2):
    return {
        'name': key,
        'old_value': value1,
        'new_value': value2,
        'type': 'mod'
    }


def no_changes(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'no_changes'
    }


def adding_comparisons(file1, file2):
    diff_add = file2.keys() - file1.keys()
    diff_remove = file1.keys() - file2.keys()
    all_keys = sorted(file1.keys() | file2.keys())

    diff = []

    for key_ in all_keys:
        value1 = file1.get(key_)
        value2 = file2.get(key_)

        if key_ in diff_add:
            diff.append(add(key_, value2))
        elif key_ in diff_remove:
            diff.append(remove(key_, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(inside(key_, value1, value2))
        elif value1 != value2:
            diff.append(modified(key_, value1, value2))
        else:
            diff.append(no_changes(key_, value1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff
