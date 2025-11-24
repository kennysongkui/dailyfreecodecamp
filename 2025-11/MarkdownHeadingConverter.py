'''
Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
'''

import re


def convert(heading):
    result = 'Invalid format'
    test = re.search('# ', heading)
    if test == None:
        heading = result
        return heading
    flag = test.end()
    last_str = heading[flag:].lstrip()
    start_str = heading[:flag]
    str_len = len(start_str.replace(" ", ""))
    if str_len > 6:
        heading = result
        return heading
    heading = '<h{}>{}</h{}>'.format(str_len, last_str, str_len)
    return heading

#
# t1 = convert("# My level 1 heading")
# print(t1)

# t2 = convert("My heading")
# print(t2)

t3 = convert("  ###  My level 3 heading")
print(t3)