'''
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.
'''


def difference(arr1, arr2):
    new_arr = arr1 + arr2
    unique_list = list(set(new_arr))
    print(unique_list)
    for i in range(len(arr1)):
        if arr1[i] in arr1 and arr1[i] in arr2:
            unique_list.pop(unique_list.index(arr1[i]))

    arr1 = sorted(unique_list, key=lambda x: str(x))
    print(arr1)
    return arr1


# t  = difference([1, 2, 3], [3, 4, 5])
# print(t)

t1 = difference([1, "a", 2], [2, "b", "a"])
print(t1)

# t2 = difference(["a", "b"], ["c", "b"])
# print(t2)
