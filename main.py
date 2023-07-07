import sys
import json
from modules.labyrinth import Labyrinth

def check_validity(labyrinth) -> bool:
    if isinstance(labyrinth, list) and 3 <= len(labyrinth) and len(labyrinth) <= 1000:
        
        row_length = len(labyrinth[0])
        for row in labyrinth:
            this_row_length = len(row)
            if (not isinstance(row, list)) or 3 > this_row_length or this_row_length > 1000 or row_length != this_row_length:
                return False
        
        return True
    
    return False


data = sys.stdin.readlines()
try:
    data = json.loads("".join([x.split("\n")[0] for x in data]))
    if not check_validity(data):
        raise Exception("Input not valid")
except Exception as e:
    print(f"Error while loading the labyrinth: {e}")
    exit(-1)

try:
    lab = Labyrinth(data)

    print(lab.simple_a_star())
except Exception as e:
    print(f"Error while trying to find the number of movements: {e}")