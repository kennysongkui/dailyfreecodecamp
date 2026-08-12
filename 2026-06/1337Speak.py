'''
1337 Speak
Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

Letter	Leet
a	4
e	3
g	9
i	1
l	1
o	0
s	5
t	7
Characters with no substitution are left unchanged.
'''


def make_leet(s):
    letter_to_leet = {
        'a': 4,
        'e': 3,
        'g': 9,
        'i': 1,
        'l': 1,
        'o': 0,
        's': 5,
        't': 7
    }

    chars = []
    for i in s:
        print(i)
        if i not in letter_to_leet.keys():
            chars.append(i)
        else:
            chars.append(str(letter_to_leet[i]))
    print(chars)
    result = ''.join(chars)
    print(result)
    s = result
    return s


t = make_leet("cool")
print(t)
