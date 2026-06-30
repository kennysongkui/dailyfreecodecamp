'''
Word Score
Given a word, return its score using a standard letter-value table:

Letter	Value
A	1
B	2
...	...
Z	26
Upper and lowercase letters have the same value.
'''


def get_word_score(word):
    # print(ord("A"))
    new_arr = list(word)
    print(new_arr)
    sum = 0
    for i in new_arr:
        sum += ord(i.upper()) - 64
    print(sum)

    word = sum
    return word


t = get_word_score("hi")
print(t)
