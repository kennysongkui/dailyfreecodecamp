'''
Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.
'''


def count_characters(sentence):
    new_dict = {}
    for i in sentence:
        i = i.lower()
        if i.isalpha():
            if i in new_dict.keys():
                new_dict[i] += 1
            else:
                new_dict.update({i: 1})
    sorted_dict = {}
    for key in sorted(new_dict.keys()):
        sorted_dict[key] = new_dict[key]
    # print(type(sorted_dict))
    new_arr = []
    for k, v in sorted_dict.items():
        new_arr.append(k + " " + str(v))
    # print(new_dict)
    print(new_arr)
    sentence = new_arr
    # sentence = '[' + ', '.join(f'"{item}"' for item in new_arr) + ']'
    return sentence


# t = count_characters("hello world")
# print(t)

t1 = count_characters("// TODO: Complete this challenge ASAP!")
print(t1)
