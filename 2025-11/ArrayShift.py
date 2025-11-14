'''
Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
'''

def shift_array(arr, n):
    arr_len = len(arr)
    new_arr = []
    if n > 0:
       i = n % arr_len
       new_arr = arr[i:] +arr[:i]
    elif n < 0:
        j = arr_len - (abs(n) % arr_len)
        # arr = arr[::-1]
        print(j)
        print(arr[:], arr[j:])
        new_arr =arr[j:] + arr[:j]

    print(new_arr)

    print(arr_len)
    arr = new_arr[:]
    return arr

# t = shift_array([1, 2, 3], 1)
# print(t)

# t1 = shift_array(["alpha", "bravo", "charlie"], 5)
# print(t1)

t2 = shift_array([1, 2, 3], -1)
print(t2)