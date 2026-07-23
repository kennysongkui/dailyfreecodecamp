'''
I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

If a word contains "ei" not preceded by "c", replace it with "ie".
If a word contains "ie" preceded by "c", replace it with "ei".
All other words are left unchanged.
'''


def i_before_e(sentence):
    words = sentence.split()
    corrected_words = []

    for word in words:
        chars = list(word)
        i = 0
        while i < len(chars) - 1:
            first = chars[i].lower()
            second = chars[i + 1].lower()

            if first == 'e' and second == 'i':
                if i == 0 or chars[i - 1].lower() != 'c':
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 1
            elif first == 'i' and second == 'e':
                if i > 0 and chars[i - 1].lower() == 'c':
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    i += 1
            i += 1

        corrected_words.append(''.join(chars))

    result = ' '.join(corrected_words)
    print(result)

    sentence = result
    return sentence


t = i_before_e("beleive")
print(t)
