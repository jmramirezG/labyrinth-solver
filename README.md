# Labyrinth Solver

* Input: List[List[str]] where the character "." means the cell is empty and "#" means the cell is blocked.
  
  [3, 3] < size < [1000, 1000].

  The input comes from stdin (for testing purposes), so we need to run the program as follows:
  
  ```bash
  python3 main.py
  [[".",".",".",".",".",".",".",".","."],
  ["#",".",".",".","#",".",".",".","."],
  [".",".",".",".","#",".",".",".","."],
  [".","#",".",".",".",".",".","#","."],
  [".","#",".",".",".",".",".","#","."]]
  <Ctrl+d>
  ```

* Output: integer number representing the lowest amount of moves required to solve the labyrinth.
  
  If impossible to solve, we return -1.

The "player" occupies 3 cells in a line (limited to horizontal or vertical orientation).

We always start horizontally with our first cell in position [0, 0].

The goal is to get one of our cells in position [n, n], (bottom-right corner).

Possible moves the player can perform are:

* Move right.
* Move left.
* Move up.
* Move down.
* Rotate.

To move we need to make sure the cells in the direction we are moving are available (empty).

To rotate we need a 3x3 square of empty cells.
