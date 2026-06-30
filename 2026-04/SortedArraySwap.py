'''
Sorted Array Swap
Given an array of integers, return a new array using the following rules:

Sort the integers in ascending order
Then swap all values whose index is a multiple of 3 with the value before it.

'''

def sort_and_swap(arr):

    arr = sorted(arr)

    new_arr = []

    for i in range(len(arr)):
        new_arr.append(arr[i])
        if i % 3 == 0:
            x = new_arr[i -1]
            new_arr[i-1] = new_arr[i]
            new_arr[i] = x

    print(new_arr)
    arr = new_arr
    return arr

t = sort_and_swap([3, 1, 2, 4, 6, 5])
print(t)