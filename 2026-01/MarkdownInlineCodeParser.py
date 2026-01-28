'''
Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

Return the given string with all code blocks converted to HTML code tags.

For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.


'''

import  re

def parse_inline_code(markdown):
    pattern = r'\`([^`]+)\`'

    result = re.sub(pattern, r'<code>\1</code>',markdown)
    print(result)
    markdown = result

    return markdown


# t = parse_inline_code("Use `let` to declare the variable.")
# print(t)

t1 = parse_inline_code("Use `let` or `const` to declare a variable.")
print(t1)