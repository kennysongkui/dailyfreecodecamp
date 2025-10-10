'''
Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.
'''

def get_longest_word(sentence):
    arr = sentence.split()
    sentence = arr[0]
    for i in arr:
        e = i.maketrans("", "", ".")
        y = i.translate(e)
        if len(y) > len(sentence):
            sentence = y
    return sentence

t = get_longest_word("coding is fun")
print(t)
t1 = get_longest_word("Coding challenges are fun and educational.")
print(t1)