'''
Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
'''


def is_match(fingerprint_a, fingerprint_b):
    result = True
    if len(fingerprint_a) == len(fingerprint_b):
        str_len = len(fingerprint_a)
        count = 0
        for i in range(str_len):
            if fingerprint_a[i] != fingerprint_b[i]:
                count += 1
        precent = count / str_len
        if precent > 0.1:
            result = False
        print(precent)
    else:
        result = False
    fingerprint_a = result
    return fingerprint_a


t = is_match("helloworld", "jelloworld")
print(t)
