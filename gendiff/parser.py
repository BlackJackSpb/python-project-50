import json
import yaml


def get_data(path):
    if path.endswith('.json'):
        return parse(path, 'json')
    elif (path.endswith('.yml') or path.endswith('.yaml')):
        return parse(path, 'yml')


def parse(content, format):
    if format == 'json':
        with open(content) as f:
            return json.load(f)
    elif format == 'yml':
        with open(content) as f:
            return yaml.safe_load(f)
