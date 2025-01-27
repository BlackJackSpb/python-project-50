import json
import yaml


def parser_json(file):
    with open(file) as f:
        return json.load(f)


def parser_yaml(file):
    with open(file) as f:
        return yaml.safe_load(f)


def parsers(path):
    if path.endswith('.json'):
        return parser_json(path)
    elif (path.endswith('.yml') or path.endswith('.yaml')):
        return parser_yaml(path)
