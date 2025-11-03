'''
Word Counter
Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.
'''

def count_words(sentence):
    new_list = sentence.split()
    # print(len(new_list))
    sentence = len(new_list)
    return sentence


t = count_words("The missing semi-colon crashed the entire internet.")
print(t)
