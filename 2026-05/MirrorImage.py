'''
Mirror Image
Given two strings, determine if the second string is a mirror image of the first.

A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.

Symmetric characters look like themselves in a mirror:
W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ( ).

Mirrored pairs swap with each other in a mirror:
Character	Swaps with
[	]
{	}
<	>
b	d
p	q
(	)
If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.

For example, the mirrored image of "[HOW]" is "[WOH]".
'''

# def is_mirror_image(s1, s2):
#
#     s3 = quchong(s1)
#     s4 = quchong(s2)
#
#     s5 = s4[::-1]
#     print(s3)
#     if s3 == s5:
#         return True
#     else:
#         return False
#
#     return s1
#
# def quchong(s):
#     char_set = ('[', ']', '{', '}', '<', '>', 'b', 'd', 'p', 'q', '(', ')')
#     new_arr = []
#     for i in s:
#         if i not in char_set:
#             new_arr.append(i)
#
#     result = ''.join(new_arr)
#     print(result)
#     return result

def is_mirror_image(s1, s2):
    symmetric = set("WTY UIOHAXVMwoxv08=+:|-_*^! .")

    pairs = {
        '[': ']', ']': '[',
        '{': '}', '}': '{',
        '<': '>', '>': '<',
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        '(': ')', ')': '('
    }

    valid_chars = symmetric | set(pairs.keys())| set(pairs.values())

    if len(s1) != len(s2):
        return False

    if any(c not in valid_chars for c in s1) or any(c not in valid_chars for c in s2):
        return False

    def mirror(c):
        if c in symmetric:
            return c
        return pairs[c]
    mirrored_s1 = ''.join(mirror(c) for c in reversed(s1))

    if mirrored_s1 == s2:
        return True
    else:
        return False

    return s1
t = is_mirror_image("[HOW]", "[WOH]")
print(t)