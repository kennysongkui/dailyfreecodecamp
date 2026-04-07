'''
Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]
Return:

[
  ["b", "a"],
  ["b", "b"]
]
'''

def invert_matrix(matrix):

    flat = [item for row in matrix for item in row]

    print(flat)
    unique_vals = set(flat)
    print(unique_vals)
    val1, val2 = unique_vals

    swapped =[
        [val2 if elem == val1 else val1 for elem in row]
        for row in matrix
    ]
    print(swapped)
    matrix = swapped

    return matrix

t = invert_matrix([["a", "b"], ["a", "a"]])
print(t)