'''
ISBN-10 Validator
Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

The first 9 characters must be digits, and
The final character may be a digit or the letter "X", which represents the number 10.
To validate it:

Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
Add all the results together.
If the total is divisible by 11, it's valid.
'''

def is_valid_isbn10(s):
    new_arr = []
    for i in s[:-1]:
        if i == "X":
            return False
        if i != '-':
            new_arr.append(i)

    if s[-1] == "X":
        total = 100
    else:
        total = int(s[-1]) * 10
    print(total)
    for i in range(9):
        total += int(new_arr[i]) * (i+1)
        print(i, total)

    print(total)
    if total % 11 == 0:
        return True
    else:
        return False

    print(new_arr)


    return s

t = is_valid_isbn10("0-306-40615-2")
print(t)