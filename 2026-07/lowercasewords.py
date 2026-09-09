'''
lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.
'''

def get_lowercase_words(s):

    result = []

    new_arr = s.split()
    for i in new_arr:
        if i.islower():
            result.append(i)
    print(result)
    s = ' '.join(result)
    return s


t = get_lowercase_words("hello GOOD world")
print(t)