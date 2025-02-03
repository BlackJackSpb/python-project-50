import json
import yaml
import os


def get_data(path):
    with open(path) as file:
        data = file.read()
        _, format = os.path.splitext(path)
        return parse(data, format)


def parse(content, format):
    if format == '.json':
        return json.loads(content)
    elif format in ['.yaml', '.yml']:
        return yaml.safe_load(content)
    else:
        raise ValueError("Not found such extension")
