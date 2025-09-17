'''
Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
'''
def array_diff(arr1, arr2):
    arr3 = []
    for arr in arr2:
        if arr not in arr1:
            arr3.append(arr)
    for arr in arr1:
        if arr not in arr2:
            arr3.append(arr)
    arr1.clear()
    arr3.sort()
    arr1 = arr3[:]
    # for x in arr4:
    #     arr1.append(x)
    # print(arr1)
    # print(arr3)

    return arr1

# test = array_diff(["apple", "banana"], ["apple", "banana", "cherry"])
test = array_diff(["apple", "banana", "cherry"], ["apple", "banana"])
print(test)

test1 = array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])
print(test1)

test2 = array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"])
print(test2)
