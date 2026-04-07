'''
Word Length Converter
Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.
For example, given "hello world", return "5 5".
'''

def convert_words(s):
    new_arr = s.split()
    count_arr = []
    for i in new_arr:
        count_arr.append(str(len(i)))

    print(count_arr)
    result = " ".join(count_arr)
    print(result)
    s = result
    return s

t = convert_words("hello world")
print(t)