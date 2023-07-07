class NodeLab:

    def __init__(self, pos, direction, cost) -> None:
        self._pos = pos # Center cell, tuple
        self._direction = direction # "h" or "v", horizontal or vertical
        self._cost = cost   # Movements from start
    
    def __str__(self) -> str:
        return str(self._pos)

    def __eq__(self, __value: object) -> bool:
        return (isinstance(__value, NodeLab) and self._pos == __value._pos and self._direction == __value._direction)   # Check for node equality using position and direction

    def __hash__(self) -> int:
        return (self._pos[0] * 10000 + self._pos[1]) * (-1 if self._direction == "h" else 1)    # Hash func to avoid collision
    
    def can_rotate(self, labyrinth) -> bool:
        if (self._pos[0] > 0 and self._pos[0] < len(labyrinth) - 1 and self._pos[1] > 0 and self._pos[1] < len(labyrinth[0]) - 1):

            # Only check the corners, and positions we are not using depending on direction
            # Could be improved by checking parent, but won´t be noticeable with current problem constraints

            return (labyrinth[self._pos[0] - 1][self._pos[1] - 1] != "#" and 
                    labyrinth[self._pos[0] + 1][self._pos[1] - 1] != "#" and 
                    labyrinth[self._pos[0] - 1][self._pos[1] + 1] != "#" and 
                    labyrinth[self._pos[0] + 1][self._pos[1] + 1] != "#" and 
                        ((labyrinth[self._pos[0]][self._pos[1] - 1] != "#" and # Check left and right if we are vertical
                        labyrinth[self._pos[0]][self._pos[1] + 1] != "#") 
                        if self._direction == "v" else
                        (labyrinth[self._pos[0] - 1][self._pos[1]] != "#" and # Else check up and down
                        labyrinth[self._pos[0] + 1][self._pos[1]] != "#"))
                    )

        return False
    
    def get_available_moves(self, labyrinth):

        available_moves = []

        # The order in which we check available operations matter, favouring going right, down and rotating, as we want to get to the bottom-right corner
        if self._direction == "h":

            # If we are horizontally placed, moving right or left is quite simple

            if (self._pos[1] + 1 < len(labyrinth[0]) - 1 and labyrinth[self._pos[0]][self._pos[1] + 2] != "#" ):
                available_moves.append("right")

            if (self._pos[0] < len(labyrinth) - 1 and labyrinth[self._pos[0] + 1][self._pos[1]] != "#" and labyrinth[self._pos[0] + 1][self._pos[1] - 1] != "#" and labyrinth[self._pos[0] + 1][self._pos[1] + 1] != "#"):
                available_moves.append("down")

            if self.can_rotate(labyrinth):
                available_moves.append("rotate")

            if (self._pos[0] > 0 and labyrinth[self._pos[0] - 1][self._pos[1]] != "#" and labyrinth[self._pos[0] - 1][self._pos[1] - 1] != "#" and labyrinth[self._pos[0] - 1][self._pos[1] + 1] != "#"):
                available_moves.append("up")
            
            if (self._pos[1] - 1 > 0 and labyrinth[self._pos[0]][self._pos[1] - 2] != "#"):
                available_moves.append("left")
        else:
            
            # If we are vertically placed, moving up and down is quite simple

            if (self._pos[1] < len(labyrinth[0]) - 1 and labyrinth[self._pos[0]][self._pos[1] + 1] != "#" and labyrinth[self._pos[0] - 1][self._pos[1] + 1] != "#" and labyrinth[self._pos[0] + 1][self._pos[1] + 1] != "#"):
                available_moves.append("right")

            if (self._pos[0] + 1 < len(labyrinth) - 1 and labyrinth[self._pos[0] + 2][self._pos[1]] != "#"):
                available_moves.append("down")

            if self.can_rotate(labyrinth):
                available_moves.append("rotate")

            if (self._pos[0] - 1 > 0 and labyrinth[self._pos[0] - 2][self._pos[1]] != "#"):
                available_moves.append("up")
            
            if (self._pos[1] > 0 and labyrinth[self._pos[0]][self._pos[1] - 1] != "#" and labyrinth[self._pos[0] - 1][self._pos[1] - 1] != "#" and labyrinth[self._pos[0] + 1][self._pos[1] - 1] != "#"):
                available_moves.append("left")

        return available_moves
