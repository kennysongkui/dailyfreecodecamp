'''
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".


'''

from collections import Counter


def compress_string(sentence):
    new_arr = sentence.split()
    counter = Counter(new_arr)
    arr_new = []
    for i in range(len(new_arr)):
        if new_arr[i] not in arr_new:
            arr_new.append(new_arr[i])
    test_arr = []
    for i in arr_new:
        print(counter[i])
        if counter[i] > 1:
            test_arr.append(i + "(" + str(counter[i]) + ")")
        else:
            test_arr.append(i)
    print(new_arr, counter, arr_new, test_arr)
    sentence = ' '.join(test_arr)
    print(sentence)
    return sentence


t = compress_string("yes yes yes please")
print(t)
