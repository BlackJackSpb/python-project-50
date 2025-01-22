def make_plain(data, path=''):
    result = []
    children = data.get('children')
    for item in children:
        key = item.get('name')
        type = item.get('type')
        value = to_str(item.get('value'))
        new = to_str(item.get('new_value'))
        old = to_str(item.get('old_value'))
        current_path = f"{path}.{key}" if path else key
        if type == 'add':
            result.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        if type == 'remove':
            result.append(f"Property '{current_path}' was removed")
        if type == 'inside':
            result.append(f"{make_plain(item, current_path)}")
        if type == 'mod':
            result.append(
                f"Property '{current_path}' was updated. From {old} to {new}"
            )
    format = "\n".join(result)
    return f"{format}"


def to_str(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if isinstance(value, (dict, list)):
        return '[complex value]'
    return f"'{value}'"
