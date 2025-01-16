import json
import yaml


def parsers(path):
    if path.endswith('.json'):
        with open(path) as f:
            return json.load(f)
    elif (path.endswith('.yml') or path.endswith('.yaml')):
        with open(path) as f:
            return yaml.safe_load(f)
