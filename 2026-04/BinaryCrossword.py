'''
Binary Crossword
Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0
For example, "A" has the binary representation 01000001, which appears in the first row from left to right.
'''


def is_in_crossword(char):
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]

    target = format(ord(char), '08b')

    rows = [''.join(str(bit) for bit in row) for row in grid]
    print(rows)
    cols = [''.join(str(grid[r][c]) for r in range(8)) for c in range(8)]
    print(cols)
    candidates = rows + cols
    print(candidates)

    for s in candidates:
        if s == target or s[::-1] == target:
            return True
    char = False
    return char


t = is_in_crossword("I")
print(t)
