'''
Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged.
'''

def capitalize_fibonacci(s):
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    n = len(s)
    new_arr= []
    for i in range(n):
        if s[i].isalpha() and i in fib_sequence:
            new_arr.append(s[i].upper())
        elif s[i].isalpha():
            new_arr.append(s[i].lower())
        else:
            new_arr.append(s[i])

    result = ''.join(new_arr)
    print(result)
    s = result
    return s

t = capitalize_fibonacci("hello world")
print(t)