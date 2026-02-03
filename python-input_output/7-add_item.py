#!/usr/bin/python3
"""
7. Load, add, save
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    js = load_from_json_file("add_item.json")
except (FileNotFoundError, Exception):
    js = []
js.extend(sys.argv[1:])
save_to_json_file(js, "add_item.json")
