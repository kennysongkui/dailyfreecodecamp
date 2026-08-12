'''
Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

Duplicate characters in the second string are counted separately.
'''

def duplicate_character_count(str1, str2):

    count = 0
    for i in str2:
        if i in str1:
            count += 1

    print(count)
    str1 = count
    return str1

t = duplicate_character_count("aloha", "hei")
print(t)