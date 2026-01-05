'''
SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)
'''
import re


def to_screaming_snake_case(variable_name):
    result = None
    # result_arr = []
    # if "_" in variable_name:
    #     new_arr = variable_name.split("_")
    #     for i in new_arr:
    #         i = i.upper()
    #         result_arr.append(i)
    #
    # if "-" in variable_name:
    #     new_arr= variable_name.split("-")
    #     for i in new_arr:
    #         i = i.upper()
    #         result_arr.append(i)
    #
    #
    # result = "_".join(result_arr)
    variable_name = variable_name.replace('-', '_')
    print(variable_name)
    result = re.sub(r'([a-z])([A-Z])', r'\1_\2', variable_name)
    print(variable_name, result)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', result)
    print(result)
    result = result.upper()
    print(result)

    variable_name = result
    return variable_name


t = to_screaming_snake_case("user_id")
print(t)

t1 = to_screaming_snake_case("userEmail")
print(t1)

t2 = to_screaming_snake_case("user-address")
print(t2)
