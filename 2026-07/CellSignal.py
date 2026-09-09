'''
Cell Signal
Given a grid containing three cell tower readings, determine the location of the phone.

Each cell in the grid is either 0 (no tower) or a positive integer representing the number of cells to the phone, measured in a straight line: horizontal, vertical, or diagonal.
Return the [row, col] of the cell that is the correct number of cells from all three towers.
There is always exactly one solution.
'''

def find_signal(grid):

    towers = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != 0:
                towers.append((i, j, val))

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            match = True
            for tr, tc, dist in towers:
                if max(abs(r -tr), abs(c - tc)) != dist:
                    match = False
                    break
            if match:
                return [r, c]

    return grid

t = find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]])
print(t)