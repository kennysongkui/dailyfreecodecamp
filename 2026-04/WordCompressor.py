'''
Word Compressor
Given a string, return a compressed version of the string using the following rules:

The first occurrence of a word remains unchanged.
Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
Words are separated by a single space.
For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".
'''


def compress(s):
    new_arr = s.split()
    # print(new_arr)

    new_dict = {}
    result_arr = []

    for i in new_arr:
        if i not in new_dict:
            new_dict[i] = len(new_dict) + 1
            result_arr.append(i)
        else:
            result_arr.append(str(new_dict[i]))

    print(new_dict)
    print(result_arr)
    result = " ".join(result_arr)
    print(result)
    s = result

    return s


# t = compress("practice makes perfect and perfect practice makes perfect")
# print(t)

t1 = compress(
    "lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")
print(t1)
