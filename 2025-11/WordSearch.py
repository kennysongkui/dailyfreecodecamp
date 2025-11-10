'''
Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
'''


def find_word(matrix, word):
    result = []
    if not matrix or not word:
        return []

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check_direction(i, j, dx, dy):
        for k in range(len(word)):
            ni, nj = i + k * dx, j + k * dy
            if ni < 0 or ni >= rows or nj < 0 or nj >= cols or matrix[ni][nj] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                end_i = i + (len(word) - 1) * dx
                end_j = j + (len(word) - 1) * dy
                if 0 <= end_i < rows and 0 <= end_j < cols and check_direction(i,j,dx,dy):
                    result = [[i,j],[end_i, end_j]]

    print(result)

    matrix = result
    return matrix


t = find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat")
print(t)
