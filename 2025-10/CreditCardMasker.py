'''
Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
'''
import re
def mask(card):
    flag = card[4]

    if flag == " ":
        new_list = card.split()
    else:
        new_list = card.split(flag)
    # print(flag)
    for i in range(len(new_list) -1):
        new_list[i] = re.sub(r"\d", "*", new_list[i])
        # print(new_list[i])
    card = flag.join(new_list)
    # print(new_list)
    return card

t = mask("4012-8888-8888-1881")
print(t)

t1 = mask("5105 1051 0510 5100")
print(t1)