'''
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
'''

import re

def longest_word(sentence):
    result = ""
    new_arr = sentence.split()
    for i in new_arr:
        i = re.sub(r'[^\w\w]','',i)
        if len(i) > len(result):
            result = i
    print(result)
    sentence = result
    return sentence


t = longest_word("The quick red fox")
print(t)
