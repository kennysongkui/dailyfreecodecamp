'''
HTML Content Extractor
Given a string of HTML, return the plain text content with all tags removed.
'''

import re


def extract_content(html):
    pattern = r'[<](.*?)[>]'

    p = re.compile(pattern, re.S)
    new_str = re.sub(p, '', html)
    print(new_str)
    html = new_str
    return html


t = extract_content('<p>hello world</p>')
print(t)
