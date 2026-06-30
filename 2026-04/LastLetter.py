'''
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

If two or more letters tie for the last in the alphabet, return the first one.
Ignore all non-letter characters.

'''

def get_last_letter(s):

    # print(ord(s[0]))

    print(ord("W"))
    print(ord('r'))

    flag = 0
    flag_char = None

    for i in s:
        if i.isalpha():
            val = ord(i.lower()) - ord('a')
            if val > flag:
                flag = val
                flag_char = i

    # print(chr(flag))
    s = flag_char
    return s

# t = get_last_letter("world")
# print(t)

t1 = get_last_letter("Hello World")
print(t1)