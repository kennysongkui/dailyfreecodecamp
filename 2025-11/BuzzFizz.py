'''
BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.
'''

def is_fizz_buzz(sequence):
    arr_len = len(sequence)
    # last_one = sequence[-1]
    # print(arr_len, last_one)

    new_arr = []
    for i in range(arr_len):
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
    result= True
    for i in range(arr_len):
        if new_arr[i] != sequence[i] :
            return False
    sequence = result
    return sequence

t = is_fizz_buzz([1, 2, "Fizz", 4])
print(t)