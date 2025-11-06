'''
Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
'''

def build_matrix(rows, cols):
    new_list = []
    for i in range(rows):
        test_list = []
        for j in range(cols):
            test_list.append(0)
        new_list.append(test_list)
    print(new_list)
    rows = new_list[:]
    return rows

t = build_matrix(2, 3)
print(t)

t1 = build_matrix(9, 1)
print(t1)