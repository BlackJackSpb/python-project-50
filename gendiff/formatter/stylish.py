def to_str(item):
        return str(item).lower()

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
    pass