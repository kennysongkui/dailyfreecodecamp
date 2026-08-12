'''
Number Sort
Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest.
'''


def sort_numbers(s):
    sort_arr = s.split(",")
    print(sort_arr)

    int_arr = [int(i) for i in sort_arr]

    result = sorted(int_arr)
    print(result)
    s = result
    return s


t = sort_numbers("3,1,2")
print(t)
