'''
Odd Words
Given a string of words, return only the words with an odd number of letters.

Words in the given string will be separated by a single space.
Return the words separated by a single space.

'''


def get_odd_words(s):
    new_arr = s.split()
    result_arr = []
    for i in new_arr:
        if len(i) % 2 != 0:
            result_arr.append(i)

    print(result_arr)
    result = ' '.join(result_arr)
    s = result
    print(result)
    return s


t = get_odd_words("This is a super good test")
print(t)
