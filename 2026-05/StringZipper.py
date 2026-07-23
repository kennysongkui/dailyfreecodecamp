'''
String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.

Begin with the first character of the first string.
'''


def zip_strings(a, b):
    new_arr = []
    str_len = len(a)
    b_len = len(b)
    for i in range(str_len):
        new_arr.append(a[i])
        if b[i] is None:
            continue
        else:
            new_arr.append(b[i])

    print(new_arr)
    print(b[-(b_len - str_len):])

    if b_len > str_len:
        result = ''.join(new_arr) + b[-(b_len - str_len):]
    else:
        result = ''.join(new_arr)
    print(result)
    a = result
    return a


# t = zip_strings("abc", "123")
# print(t)

# t1 = zip_strings("day", "night")
# print(t1)

t2 = zip_strings("python", "javascript")
print(t2)