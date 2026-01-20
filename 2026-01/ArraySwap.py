'''
Array Swap
Given an array with two values, return an array with the values swapped.

For example, given ["A", "B"] return ["B", "A"].
'''


def array_swap(arr):
    arr_len = len(arr)
    print(arr_len)
    new_arr = []
    for i in range(arr_len):
        print(arr_len - 1 - i)
        new_arr.append(arr[arr_len - 1 - i])

    print(new_arr)
    arr = new_arr

    return arr


t = array_swap(["A", "B"])
print(t)
