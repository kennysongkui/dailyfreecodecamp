'''
Anagram Groups
Given an array of words, return a 2d array of the words grouped into anagrams.

Words are anagrams if they contain the same letters in any order.
Each word belongs to exactly one group.
Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].
'''

from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    print(groups)

    for word in words:
        key = ''.join(sorted(word))
        print(key)
        groups[key].append(word)
    result = list(groups.values())
    print(result)

    words = result
    return words


t = group_anagrams(["listen", "silent", "hello", "enlist", "world"])
print(t)
