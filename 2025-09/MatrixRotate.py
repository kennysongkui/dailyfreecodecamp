'''
Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:

1	2
3	4
You should return [[3, 1], [4, 2]], which looks like this:

3	1
4	2

'''

def rotate(matrix):
    new_arr = matrix[::-1]
    arr = []
    for i in zip(*new_arr):
       arr.append(list(i))

    matrix = arr
    return matrix

t = rotate([[1, 2], [3, 4]])
print(t)

t1 = rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(t1)