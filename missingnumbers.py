'''
Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.
'''


def find_missing_numbers(arr):
    test = arr
    test_max = max(test)
    test_min = min(test)
    test_arr =[]
    for num in range(test_min, test_max):
        if num not in test:
            test_arr.append(num)
    arr = test_arr[:]
    return arr

t = find_missing_numbers([1, 3, 5])
print(t)
t1 = find_missing_numbers([1, 2, 3, 4, 5])
print(t1)