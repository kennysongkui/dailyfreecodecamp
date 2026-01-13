'''
vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged.
'''


def vowel_case(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    new_arr = s.split()
    new_arr2 = []
    for i in new_arr:
        new_str = []
        for j in i:
            if j.isalpha():
                j = j.lower()
                print(j)
            else:
                pass
            if j in vowels_list:
                j = j.upper()

            new_str.append(j)
        new_arr2.append(''.join(new_str))

    print(new_arr2)
    print(new_arr)
    s = ' '.join(new_arr2)
    return s


# t = vowel_case("vowelcase")
# print(t)

t1 = vowel_case("HELLO, world!")
print(t1)
