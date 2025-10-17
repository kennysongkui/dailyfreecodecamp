'''
HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".
'''

import re
def strip_tags(html):
    new_html = re.sub(r'<[^>]+>','',html)
    # print(new_html)
    html = new_html
    return html


# t = strip_tags('<a href="#">Click here</a>')
#
# print(t)

t1 = strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>')
print(t1)