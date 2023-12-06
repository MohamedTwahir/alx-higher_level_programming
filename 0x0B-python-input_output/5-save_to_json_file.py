#!/usr/bin/python3
"""text file from json"""
import json


def save_to_json_file(my_obj, filename):
    """ouputs a json in text format"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
