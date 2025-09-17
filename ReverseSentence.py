

'''
Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
'''

def reverse_sentence(sentence):
    s = sentence.split()
    s.reverse()
    sentence = " ".join(s)

    return sentence

test = reverse_sentence("world hello")
print(test)
test1 = reverse_sentence("push commit git")
print(test1)
test2 = reverse_sentence("npm  install   apt    sudo")
print(test2)
test3 = reverse_sentence("import    default   function  export")
print(test3)
