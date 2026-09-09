'''
Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.

Use a golden ratio of 1.618
Allow a tolerance of 0.01
'''


def is_golden_ratio(a, b):
    if a > b:
        ratio = round(a / b, 3)
    else:
        ratio = round(b / a, 3)

    print(ratio)

    if ratio >= 1.608 and ratio <= 1.628:
        return True
    else:
        return False
    return a


# t = is_golden_ratio(21, 34)
# print(t)

t1 = is_golden_ratio(8, 13)
print(t1)
