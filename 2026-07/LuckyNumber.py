'''
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.
'''


def get_lucky_number(name):
    parts = name.split()

    if len(parts) != 2:
        raise ValueError("Input must contain exactly one space separating first and last name")
    first, last = parts

    vowels = set('aeiou')

    def count_vc(s):
        v = sum(1 for ch in s.lower() if ch in vowels)
        c = sum(1 for ch in s.lower() if ch.isalpha() and ch not in vowels)
        return v, c

    first_v, first_c = count_vc(first)
    last_v, last_c = count_vc(last)

    min_v = min(first_v, last_v)
    max_v = max(first_v, last_v)
    min_c = min(first_c, last_c)
    max_c = max(first_c, last_c)

    len_first = len(first)
    len_last = len(last)
    smaller_len = min(len_first, len_last)
    larger_len = max(len_first, len_last)

    smaller_value = min_v * min_c * smaller_len
    larger_value = max_v * max_c * larger_len

    lucky = larger_value - smaller_value
    if lucky == 0:
        return 13

    name = lucky
    return name


t = get_lucky_number("John Doe")
print(t)
