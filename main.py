import sys
import json

from modules.utils import check_validity

data = sys.stdin.readlines()
try:
    data = json.loads("".join([x.split("\n")[0] for x in data]))
    if not check_validity(data):
        raise Exception("Input not valid")
except Exception as e:
    print(f"Error while loading the labyrinth: {e}")
    exit(-1)
    