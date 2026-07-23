'''
ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.

A valid ISBN-13:

Contains only digits and hyphens
Has exactly 13 digits after removing hyphens
Passes the following check:
Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
The sum of the results must be divisible by 10.
'''

def is_valid_isbn_13(s):
    arr_new = list(s)
    isbn_arr = []
    for i in arr_new:
        if i == '-' or i.isdigit():
            if i.isdigit():
                isbn_arr.append(i)
        else:
            return False
    print(len(isbn_arr))
    if len(isbn_arr) != 13:
        return False
    sum = 0
    for i in range(13):
        if i % 2 == 0:
            sum += int(isbn_arr[i])
        else:
            sum += (int(isbn_arr[i]) * 3)

    print(sum)
    if sum  % 10 == 0:
        return True
    else:
        return False

    return s

# t = is_valid_isbn_13("9780306406157")
# print(t)

t1 = is_valid_isbn_13("978-0-13-595705-9")
print(t1)