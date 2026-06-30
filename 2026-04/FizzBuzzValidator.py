'''
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.

'''

def is_fizz_buzz(arr):
    for i in range(len(arr)):
        print(arr[i])
        if isinstance(arr[i], int):
            print(arr[i])
            n = arr[i] - i
            break
    print(n)

    new= enumerate(arr, start=n)
    print(new)
    flag = True
    for i, value in new:
        # print(i, value)
        if i % 15  ==0:
            expected = "FizzBuzz"
        elif i % 3  == 0:
            expected = "Fizz"
        elif i % 5 == 0:
            expected = "Buzz"
        else:
            expected = i

        if value != expected:
            flag = False

    print(flag)

    arr = flag
    return arr

t = is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"])
print(t)

# t1 = is_fizz_buzz([13, 14, "FizzBuzz", 16, 17])
# print(t1)

t2 = is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"])
print(t2)