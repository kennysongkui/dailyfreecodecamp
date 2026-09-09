'''
Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.

The last chunk may be smaller if the array doesn't divide evenly.

'''

def chunk_array(arr, size):

    arr_len = len(arr)
    new_arr = []
    while arr_len > 0:
        new_arr.append(arr[:size])
        del arr[:size]
        arr_len -= size
    print(new_arr)
    arr = new_arr[:]
    return arr

t = chunk_array([1, 2, 3, 4, 5, 6], 3)
print(t)
