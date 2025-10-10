'''
Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
'''

import string
import re

def capitalize(paragraph):
    # text = paragraph.split()

    if " " in paragraph :
        text = paragraph.split()
        result = []
        T = False
        for i in range(0, len(text)):
            if T:
                T = False
                continue
            if i == 0:
                result.append(text[i].capitalize())
                continue
            # print(text[i][-1])
            if text[i][-1] in string.punctuation and i < len(text) - 1:
                result.append(text[i])
                result.append(text[i + 1].capitalize())
                T = True
                continue

            result.append(text[i])
            paragraph = " ".join(result)
    else:
        result = []
        text = re.split(r'([.!?]+)', paragraph)
        # pass
        for i in text:
            if i in string.punctuation:
                result.append(i)
                continue
            result.append(i.capitalize())

        paragraph = "".join(result)
    return paragraph






t = capitalize("this is a simple sentence.")
print(t)

t2 = capitalize("i did today's coding challenge... it was fun!!")
print(t2)

t3 = capitalize("there's a space before this period . why is there a space before that period ?")
print(t3)

t4= capitalize("crazy!!!strange???unconventional...sentences.")
print(t4)
t4 = capitalize("crazy!!!strange???unconventional...sentences.")
print(t4)
