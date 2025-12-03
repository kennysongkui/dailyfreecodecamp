'''
Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
'''


def to_snake(camel):
    new_arr = []
    for i in camel:
        if i.isupper():
            new_arr.append("_" + i.lower())
        else:
            new_arr.append(i)
    print(new_arr)
    camel = ''.join(new_arr)
    return camel


t = to_snake("helloWorld")
print(t)