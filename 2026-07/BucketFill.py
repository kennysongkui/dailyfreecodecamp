'''
Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.

Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid.
'''

from collections import deque


def bucket_fill(grid, pos, new_value):
    if not grid or not grid[0]:
        return grid

    rows, cols = len(grid), len(grid[0])
    sr, sc = pos

    if not (0 <= sr < rows and 0 <= sc < cols):
        return grid

    old_value = grid[sr][sc]
    if old_value == new_value:
        return grid

    result = [row[:] for row in grid]
    queue = deque([(sr, sc)])
    result[sr][sc] = new_value

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == old_value:
                result[nr][nc] = new_value
                queue.append((nr, nc))

    print(result)
    grid = result

    return grid


t = bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B")
print(t)
