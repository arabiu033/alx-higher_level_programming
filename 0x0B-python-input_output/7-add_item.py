#!/usr/bin/python3
""" json module imported """
import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


cmd = []
filename = "add_item.json"
with open(filename, mode="a", encoding="utf-8") as fil:
    if os.stat(filename).st_size == 0:
        save_to_json_file([], filename)

    cmd = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        cmd.append(sys.argv[i])

    save_to_json_file(cmd, filename)
