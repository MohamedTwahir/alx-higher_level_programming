#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """an object from a json string/deserializing"""
    return json.loads(my_str)
