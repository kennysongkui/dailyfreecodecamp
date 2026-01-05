'''
Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
'''

import re


def parse_italics(markdown):

    new_arr = markdown.split()
    for i in new_arr:
        if i == '*' or i == '_':
            return markdown

    # pattern = re.compile(r'^[\*|\_](.*)[\*|\_]\$')
    pattern = r'(?<!\S)([*_])(.*?)\1(?!\S)'

    def replace_italic(match):
        marker = match.group(1)
        content = match.group(2)
        return f'<i>{content}</i>'

    result = re.sub(pattern, replace_italic, markdown, flags=re.DOTALL)

    print(result)

    markdown = result
    return markdown


# t = parse_italics("*This is italic*")
# print(t)

# t1 = parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.")
# print(t1)
t2 = parse_italics("*This is not italic *")
print(t2)
