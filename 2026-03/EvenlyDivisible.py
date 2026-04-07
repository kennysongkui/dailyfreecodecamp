'''
Evenly Divisible
Given two integers, determine if you can evenly divide the first one by the second one.
'''

def is_evenly_divisible(a, b):

    if a % b == 0:
        return True
    else:
        return False

    return a

t = is_evenly_divisible(4, 2)
print(t)