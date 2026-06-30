'''
String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

If the count of characters separating two numbers is even, use addition.
If it's odd, use subtraction.
Consecutive digits form a single number.
Operations are applied left to right.
Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.
'''
import re


def do_math(s):
    matches = list(re.finditer(r'\d+', s))

    if not matches:
        return 0

    if len(matches) == 1:
        return int(matches[0].group())

    numbers = [int(m.group()) for m in matches]
    result = numbers[0]
    print(numbers)

    for i in range(1, len(numbers)):
        prev_end = matches[i - 1].end()
        curr_start = matches[i].start()
        separator = s[prev_end:curr_start]
        sep_len = len(separator)

        if sep_len % 2 == 0:
            result += numbers[i]
        else:
            result -= numbers[i]

    print(result)
    s = result
    return s


t = do_math("3ab10c8")
print(t)
