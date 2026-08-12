'''
Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

Each cell contains "R", "Y", or "" (empty string).
Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
Return:

A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
An empty array if there is no winner.
'''


def connect_three(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(rows):
        for c in range(cols):
            piece = matrix[r][c]
            if piece == "":
                continue
            for dr, dc in dirs:
                if (0 <= r + 2 * dr < rows and 0 <= c + 2 * dc < cols and matrix[r + dr][c + dc] == piece and
                        matrix[r + 2 * dr][c + 2 * dc] == piece):
                    coords = [[r, c], [r + dr, c + dc], [r + 2 * dr, c + 2 * dc]]
                    coords.sort(key=lambda x: (x[0], x[1]))
                    return [piece] + coords

    return []


t = connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]])
print(t)
