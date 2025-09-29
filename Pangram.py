'''
Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.
'''
import sys


def is_pangram(sentence, letters):
    s = sentence.lower()
    e = s.maketrans("", "", ",.!")
    y = s.translate(e)
    for i in y:
        if i == " ":
            continue
        else:
            if letters.find(i) == -1:
                sentence = False
                return sentence
                sys.exit()
            else:
                sentence = True
    for j in letters:
        if y.find(j) == -1:
            sentence = False
            return sentence
            sys.exit()
        else:
            sentence = True

    return sentence

#
# t = is_pangram("hello", "helo")
# print(t)

# t1 = is_pangram("Hello World!", "helowrd")
# print(t1)
t2 = is_pangram("hello", "hel")
print(t2)

# t3 = is_pangram("hello", "helow")
# print(t3)