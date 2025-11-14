'''
Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
'''


def count(s):
    new_list = s.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    con_count = 0
    for i in new_list:
        for j in i:
            if j.lower() in vowels:
                vowels_count += 1
            elif j.isalpha:
                con_count += 1
            else:
                pass

    print(vowels_count, con_count)
    s = [vowels_count, con_count]
    return s


t = count("Hello World")
print(t)

t1 = count("The quick brown fox jumps over the lazy dog.")
print(t1)
