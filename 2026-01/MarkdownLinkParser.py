'''
Markdown Link Parser
Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
'''

import re

def parse_link(markdown):

    pattern = r'\[(.*)\]\((.*)\)'

    test = re.match(pattern, markdown)
    print(test.groups())

    result = '<a href="{}">{}</a>'.format(test.group(2), test.group(1))
    print(result)
    markdown = result
    return markdown


t = parse_link("[freeCodeCamp](https://freecodecamp.org/)")
print(t)