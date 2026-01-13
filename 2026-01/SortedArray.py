'''
Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted".

'''

def is_sorted(arr):
    # result = None

    new_arr = sorted(arr)
    print(arr)
    desc_arr = sorted(arr, reverse=True)
    print(desc_arr)
    if arr == new_arr:
        result = "Ascending"
    elif arr == desc_arr:
        result = "Descending"
    else:
        result = "Not sorted"

    print(result)
    arr = result

    return arr

t = is_sorted([1, 2, 3, 4, 5])
print(t)
