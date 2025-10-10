'''
2nd Largest
Given an array, return the second largest distinct number.
'''

def second_largest(arr):
    new_list = sorted(set(arr))
    arr = new_list[-2]
    return arr

t = second_largest([1, 2, 3, 4])
print(t)
t1 = second_largest([10, -17, 55.5, 44, 91, 0])
print(t1)