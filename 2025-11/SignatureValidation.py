'''
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.
'''


def verify(message, key, signature):
    letters_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
        'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
        'X': 50, 'Y': 51, "Z": 52, ' ': 0}

    total_mess = 0
    total_key = 0
    flag = False
    for i in message:
        # print(i)
        # print(letters_dict[i])
        if i.isalpha() :
            total_mess += letters_dict[i]
        else:
            continue
    for j in key:
        if j.isalpha():
            total_key += letters_dict[j]
        else:
            continue
    # print(total_mess, total_key)
    if total_key + total_mess == signature:
        flag = True

    message = flag

    return message


t = verify("foo", "bar", 57)
print(t)

t1 = verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)
print(t1)
