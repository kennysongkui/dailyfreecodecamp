'''
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.
'''

def is_flat(arr):
    for i in arr:
        if type(i) == list:
            return False
    result = True
    arr = result

    return arr

t = is_flat([1, [2, 3], 4])
print(t)
