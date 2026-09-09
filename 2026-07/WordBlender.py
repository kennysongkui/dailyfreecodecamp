'''
Word Blender
Given two words, return a new word by combining the first half of the first word with the second half of the second word.

For odd-length words, the first half is the shorter half.
'''


def blend_words(word1, word2):
    first_part = word1[:(int(len(word1) / 2))]
    print(first_part)
    print(int(5 / 2))
    # print(word1[:2])
    second_part = word2[(int(len(word2) / 2)):]
    result = first_part + second_part
    print(result)

    word1 = result
    return word1


t = blend_words("turtle", "toucan")
print(t)
