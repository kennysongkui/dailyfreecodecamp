'''
Transposed Matrix
Given a matrix (an array of arrays), return the transposed version of it.

To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1] should move to index [1, 0].

For example, given:

[
  [1, 2, 3],
  [4, 5, 6]
]
Return:

[
  [1, 4],
  [2, 5],
  [3, 6]
]
'''
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    print(rows, cols)

    new_arr = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    print(new_arr)

    matrix = new_arr
    return matrix

t = transpose([[1, 2, 3], [4, 5, 6]])
print(t)
