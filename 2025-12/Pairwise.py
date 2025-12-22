'''
Pairwise
Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

2 and 8 (2 + 8 = 10), whose indices are 0 and 4
4 and 6 (4 + 6 = 10), whose indices are 2 and 3
Add all the indices together to get a return value of 9.
'''


def pairwise(arr, target):
    result = 0
    for i in range(len(arr)):
        x = target - arr[i]
        # print(x, arr[i])
        if x in arr:
            index = arr.index(x)
            if i != index:
                result += index
                result += i
            print(result, i, index)

    print(result)
    arr = int(result / 2)

    return arr


# t = pairwise([2, 3, 4, 6, 8], 10)
# print(t)

t1 = pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24)
print(t1)