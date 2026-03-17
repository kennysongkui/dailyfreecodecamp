'''
Add Punctuation
Given a string of sentences with missing periods, add a period (".") in the following places:

Before each space that comes immediately before an uppercase letter
And at the end of the string
Return the resulting string.
'''

import re

def add_punctuation(sentences):

    corrected = re.sub(r' (?=[A-Z])', '. ', sentences)
    result = corrected + "."
    print(result)
    sentences = result
    return sentences

t = add_punctuation("Hello world It's nice today")
print(t)