#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
import json
import os.path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
args = sys.argv
my_list = []
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    my_list = load_from_json_file(filename)

for elem in sys.argv[1:]:
    my_list.append(elem)
save_to_json_file(my_list, filename)
