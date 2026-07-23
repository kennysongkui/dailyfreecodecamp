'''
Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.

If more than one element could be considered out of place, return the index of the first one.

'''


def find_offender(arr):
    index = 0
    for i in range(len(arr) -1):
        if arr[i] > arr[i + 1]:
            return i
        else:
            print(arr[i])
            continue

    return arr

#
# t = find_offender([1, 6, 2, 3, 4, 5])
# print(t)
#
# t1 = find_offender([2, 4, 1, 6, 8])
# print(t1)

t2 = find_offender([1, 2, 3, 5, 4, 5])
print(t2)