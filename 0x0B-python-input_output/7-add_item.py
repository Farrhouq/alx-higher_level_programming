#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import json

    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        list_cur = load('add_item.json')
    except json.decoder.JSONDecodeError:
        list_cur = []
    for arg in sys.argv[1:]:
        list_cur.append(arg)
    save(list_cur, 'add_item.json')
