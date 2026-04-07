'''
Pascal's Triangle Row
Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

Here's the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''


def pascal_row(n):
    new_arr = []
    # for i in range(n):
    #     print(i)
    #     new_arr.append([])
    #     new_arr[i].append(1)
    #     for j in range(1, i):
    #         new_arr[i].append(new_arr[i - 1][j - 1] + new_arr[i - 1][j])
    # print(new_arr)

    for i in range(n):
        row = [1] *(i +1)
        for j in range(1, i):
            row[j] = new_arr[i-1][j-1] + new_arr[i-1][j]
        new_arr.append(row)

    print(new_arr)
    result = new_arr[n-1]
    print(result)
    n = result
    return n


t = pascal_row(15)
print(t)
