'''
Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.
'''


def flatten(arr):
    new_arr = []
    for i in arr:
        if isinstance(i, list):
            new_arr.extend(flatten(i))
        else:

            new_arr.append(i)

        print(i)

    print(new_arr)

    arr = new_arr[:]
    return arr


#
# t = flatten([1, [2, 3], 4])
# print(t)

t1 = flatten([5, [4, [3, 2]], 1])
print(t1)
