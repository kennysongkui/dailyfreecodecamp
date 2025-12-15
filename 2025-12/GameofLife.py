'''
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.
'''


def game_of_life(grid):
    rows = len(grid)
    cols = len(grid[0])

    next_state = [[0] * cols for _ in range(rows)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):

            live_neighbors = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        live_neighbors += 1
            if grid[r][c] == 1:
                if live_neighbors < 2:
                    next_state[r][c] = 0
                elif 2 <= live_neighbors <= 3:
                    next_state[r][c] = 1
                else:
                    next_state[r][c] = 0
            else:
                if live_neighbors == 3:
                    next_state[r][c] = 1
                else:
                    next_state[r][c] = 0
    print(next_state)
    grid = next_state[:]
    return grid


t = game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]])
print(t)
