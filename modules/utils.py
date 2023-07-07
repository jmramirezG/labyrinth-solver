def check_validity(labyrinth) -> bool:
    if isinstance(labyrinth, list) and 3 <= len(labyrinth) and len(labyrinth) <= 1000:
        
        row_length = len(labyrinth[0])
        for row in labyrinth:
            this_row_length = len(row)
            if (not isinstance(row, list)) or 3 > this_row_length or this_row_length > 1000 or row_length != this_row_length:
                return False
        
        return True
    
    return False
        