import json
import yaml


def parsers(first_file, second_file):
    if first_file.endswith('.json') and second_file.endswith('.json'):
        with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
    elif (first_file.endswith('.yml') or first_file.endswith('.yaml')) and \
         (second_file.endswith('.yml') or second_file.endswith('.yaml')):
        with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
            data1 = yaml.safe_load(f1)
            data2 = yaml.safe_load(f2)
    else:
        return ('Error: Unsupported file types. Both files must be either '
                'JSON or YAML.')

    return data1, data2
