'''
Sum of Differences
Given an array of numbers, return the sum of the differences between each number and the one that follows it.

For example, given [1, 3, 4], return 3 (2 + 1).
'''


def sum_of_differences(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += (arr[i + 1] - arr[i])

    print(total)
    arr = total
    return arr


t = sum_of_differences([1, 3, 4])
print(t)
