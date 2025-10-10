'''
Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
'''

def find_landing_spot(matrix):
    first_array = []
    new_matrix = matrix[::]
    rows = len(new_matrix)
    cols = len(matrix[0])
    min_sum = float('inf')

    for i in range(rows):
        for j in range(cols):
            # print(new_matrix[i][j])
            if new_matrix[i][j] == 0:
                total =0
                if i - 1 >= 0:
                    total += matrix[i-1][j]
                if i + 1 < rows:
                    total += matrix[i+1][j]
                if j - 1>= 0:
                    total += matrix[i][j-1]
                if j + 1 < cols:
                    total += matrix[i][j+1]

                if total < min_sum:
                    min_sum = total
                    first_array = [i, j]

    matrix = first_array[:]

    return matrix


t = find_landing_spot([[1, 0], [2, 0]])
print(t)