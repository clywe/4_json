import json
from pprint import pprint


def load_data(filepath):
    with open(filepath) as json_file:
        bars = json.load(json_file)
    return bars


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    pretty_print_json(load_data("file.json"))
