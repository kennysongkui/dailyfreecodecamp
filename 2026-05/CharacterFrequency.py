'''
Character Frequency
Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.
'''

def get_frequency(s):
    test_dict = {}
    for i in list(s):
        if i in test_dict.keys():
            test_dict[i] += 1
        else:
            test_dict[i] = 1
    print(test_dict)
    s = test_dict
    return s

t = get_frequency("test")
print(t)