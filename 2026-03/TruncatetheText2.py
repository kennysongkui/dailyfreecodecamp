'''
Truncate the Text 2
Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:

Letters	Width
"ilI"	1
"fjrt"	2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4
The table above includes all upper and lower case letters. Additionally:

Spaces (" ") have a width of 2

Periods (".") have a width of 1

If the given string is 50 units or less, return the string as-is, otherwise

Truncate the string and add three periods at the end ("...") so its total width, including the three periods, is as close as possible to 50 units without going over.
'''

def truncate_text(s):

    def char_width(ch):
        if ch == " ":
            return 2
        if ch == ".":
            return 1
        if ch in "ilI":
            return 1
        if ch in "fjrt":
            return 2
        if ch in "abcdeghkmnopqrstuvwxyzJL":
            return 3
        if ch in "ABCDEFGHKMNOPQRSTUVWXYZ":
            return 4
        return 1
    total_width = sum(char_width(c) for c in s)

    if total_width <= 50:
        return s

    limit = 47
    prefix_width = 0
    prefix_chars = []

    for ch in s:
        w = char_width(ch)
        if prefix_width + w <= limit:
            prefix_width += w
            prefix_chars.append(ch)
        else:
            break
    result = ''.join(prefix_chars) + "..."
    print(result)
    s = result
    return s

t = truncate_text("The quick brown fox")
print(t)