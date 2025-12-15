'''
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.
'''

from collections import Counter


def most_frequent(arr):
    counter = Counter(arr)
    print(type(counter))
    print(counter)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1])
    a, b = sorted_counter.pop()
    arr = a

    return arr


t = most_frequent(["a", "b", "a", "c"])
print(t)
