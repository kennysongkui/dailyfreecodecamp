'''
Array Sum
Given an array of numbers, return the sum of all the numbers.

'''

def sum_array(numbers):
    result = 0
    for i in numbers:
        result += i

    print(result)
    numbers = result

    return numbers

t = sum_array([1, 2, 3, 4, 5])
print(t)