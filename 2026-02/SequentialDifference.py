'''
Sequential Difference
Given an array of numbers, return a new array containing the value needed to get from each number to the next number.

For the last number, use 0 since there is no next number.
For example, given [1, 2, 4, 7], return [1, 2, 3, 0].

'''


def find_differences(arr):
    new_arr = []
    arr_len = len(arr)
    for i in range(arr_len):
        if i < arr_len - 1:
            print(i)
            j = arr[i + 1] - arr[i]
            new_arr.append(j)
        else:
            new_arr.append(0)

    print(new_arr)

    arr = new_arr[:]
    return arr


t = find_differences([1, 2, 4, 7])
print(t)
