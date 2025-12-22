'''
Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

'''

def create_board(dimensions):
    rows, cols = dimensions
    result = [["O" for i in range(cols)] for j in range(rows) ]
    for i in range(rows):
        for j in range(cols):

            # print((i+j)//2)
            if (i + j )% 2 :
                result[i][j] = "O"
            else:
                result[i][j] = "X"
    print(rows, cols)
    print(result)
    dimensions = result[:]
    return dimensions

t = create_board([3, 3])
print(t)