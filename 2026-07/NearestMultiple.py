'''
Nearest Multiple
Given two integers, round the first to the nearest multiple of the second.
'''

def round_to_nearest_multiple(num, multiple):

    s = round(num/multiple)
    result = multiple * s
    print(result)
    num = result
    return num

t = round_to_nearest_multiple(5, 3)
print(t)