def build_ident(symbol=" "):
    return f"  {symbol} "


def make_ident(depth):
    return " " * (depth * 4)


def make_stylish(data, depth=0):
    deep_ident = make_ident(depth)
    tree = []
    children = data.get('children')
    for _item in children:
        key = _item.get('name')
        type = _item.get('type')
        value = _item.get('value')
        string = to_str(value, depth + 1)
        new = to_str(_item.get('new_value'), depth + 1)
        old = to_str(_item.get('old_value'), depth + 1)
        if type == 'add':
            tree.append(f'{deep_ident}{build_ident('+')}{key}: {string}')
        if type == 'remove':
            tree.append(f'{deep_ident}{build_ident('-')}{key}: {string}')
        if type == 'no_changes':
            tree.append(f'{deep_ident}{build_ident()}{key}: {string}')
        if type == 'inside':
            tree.append(
                f'{deep_ident}{build_ident()}{key}:' +
                f'{make_stylish(_item, depth + 1)}'
            )
        if type == 'mod':
            tree.append(f"{deep_ident}{build_ident('-')}{key}: {old}")
            tree.append(f"{deep_ident}{build_ident('+')}{key}: {new}")
    format = '\n'.join(tree)
    return f'{{\n{format}\n{deep_ident}}}'


def to_str(value, depth):
    deep_ident = make_ident(depth)
    rows = []
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        for _key, _row in value.items():
            rows.append(
                f'{deep_ident}{build_ident()}{_key}: {to_str(_row, depth + 1)}'
            )
        format = '\n'.join(rows)
        return f'{{\n{format}\n{deep_ident}}}'
    return f'{value}'
