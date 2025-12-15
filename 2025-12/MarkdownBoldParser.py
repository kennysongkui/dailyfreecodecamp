'''
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
'''

import re

def parse_bold(markdown):
    new_arr = markdown.split()
    for i in new_arr:
        if i == "**" or i == "__":
            return markdown

    pattern_asterisk = re.compile(r'\*\*([^*]+?)\*\*')
    pattern_underscore = re.compile(r'__([^_]+?)__')

    result = pattern_asterisk.sub(r'<b>\1</b>', markdown)
    result = pattern_underscore.sub(r'<b>\1</b>', result)

    print(result)
    markdown = result
    return markdown

# t = parse_bold("__This is also bold__")
# print(t)

t1 = parse_bold("**This is not bold **")
print(t1)
