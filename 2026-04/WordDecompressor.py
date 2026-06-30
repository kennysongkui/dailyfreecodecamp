'''
Word Decompressor
Given a compressed string, return the decompressed version using the following rules:

The given string is made up of words and numbers separated by spaces.
Leave the words unchanged.
Replace numbers with the word at that position, where the first word is at position 1.
For example, given "practice makes perfect and 3 1 2 3", return "practice makes perfect and perfect practice makes perfect".
'''


def decompress(s):
    new_arr = s.split()
    result_arr = []

    for i in new_arr:
        if i.isdigit():
            pos = int(i)
            word = result_arr[pos - 1]
            result_arr.append(word)
        else:
            result_arr.append(i)

    result = " ".join(result_arr)

    print(result)
    s = result
    return s


t = decompress("practice makes perfect and 3 1 2 3")
print(t)
