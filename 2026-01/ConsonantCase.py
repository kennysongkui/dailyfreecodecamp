'''
Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:

All consonants should be converted to uppercase.
All vowels (a, e, i, o, u in any case) should be converted to lowercase.
All hyphens (-) should be converted to underscores (_).
'''


def to_consonant_case(s):
    vowels = ('A', 'E', 'I', 'O', 'U')
    new_arr = list(s)

    test_arr = []

    for i in new_arr:
        if i.isalpha():
            i = i.upper()
            if i in vowels:
                i = i.lower()
        elif i == "-":
            i = "_"
        print(i)

        test_arr.append(i)

    print(test_arr)

    result = ''.join(test_arr)
    print(result)
    s = result
    return s


t = to_consonant_case("helloworld")
print(t)
