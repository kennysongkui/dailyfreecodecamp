'''
Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.
'''

def has_consonant_count(text, target):
    consonants_list = ('a', 'e', 'i', 'o', 'u')
    new_arr = list(text)
    result = 0
    for i in new_arr:
        if i.isalpha():
            if i not in consonants_list:
                result += 1
    print(result)
    print(new_arr)

    if result == target:
        text = True
    else:
        text = False
    return text

t = has_consonant_count("helloworld", 7)
print(t)