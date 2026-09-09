'''
Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:

If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".

'''

import re


def pig_latin(s):
    # vowel = ["a", "e", "i", "o","u"]
    # print(s[0])
    # if s[0].islower() in vowel:
    # # if s[0] == "u":
    #     result = s + "way"
    # else:
    #     result = None
    #
    # print(result)

    def convert_word(word):
        if not word:
            return word
        was_upper = word[0].isupper()
        lower_word = word.lower()
        vowels = set('aeiou')

        first_vowel = -1
        for i, ch in enumerate(lower_word):
            if ch in vowels:
                first_vowel = i
                break
        if first_vowel == -1:
            result = lower_word + "ay"
        elif first_vowel == 0:
            result = lower_word + "way"
        else:
            result = lower_word[first_vowel:] + lower_word[:first_vowel] + "ay"

        if was_upper:
            result = result.capitalize()

        return result

    pattern = re.compile(r'[A-Za-z]+')
    result_ok = pattern.sub(lambda m: convert_word(m.group()), s)

    print(result_ok)
    s = result_ok

    return s


t = pig_latin("universe")
print(t)
