'''
100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
'''

def one_hundred(chars):
    str_len = len(chars)
    test = 100 // str_len
    new_str = chars * (test + 1)
    print(new_str[:100], str_len, test)
    chars = new_str[:100]
    return chars

t = one_hundred("One hundred ")
print(t)