'''
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.
'''
from collections import Counter


def purge_most_frequent(arr):
    count = Counter(arr)
    max_key = max(count, key=count.get)
    print(count, max_key)
    new_arr = arr[:]
    for i in range(len(arr)):
        if arr[i] == max_key:
            new_arr.remove(arr[i])
    arr = new_arr[:]
    return arr


t = purge_most_frequent([1, 2, 2, 3])
print(t)
