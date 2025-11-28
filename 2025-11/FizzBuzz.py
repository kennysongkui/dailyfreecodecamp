'''
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".
'''


def fizz_buzz(n):
    new_arr = []
    for i in range(n):
        test = i + 1
        if test % 3 == 0 and test % 5 == 0:
            new_arr.append("FizzBuzz")
            continue
        elif test % 3 == 0:
            new_arr.append("Fizz")
        elif test % 5 == 0:
            new_arr.append("Buzz")
        else:
            new_arr.append(test)
    print(new_arr)
    n = new_arr[:]
    return n


# t = fizz_buzz(4)
# print(t)
#
# t1 = fizz_buzz(8)
# print(t1)

t2 = fizz_buzz(20)
print(t2)

t3 = fizz_buzz(50)
print(t3)
