'''
RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
'''
import re


def rgb_to_hex(rgb):
    matches = re.findall(r'\d+', rgb)
    output = ["#", ]
    for i in matches:
        # e = hex(int(i, 10))[2:]
        x = "{:02x}".format(int(i, 10))
        print(x)
        output.append(x)
        # print(e)
    rgb = ''.join(output)
    return rgb


# t = rgb_to_hex("rgb(255, 255, 255)")
# print(t)
t1 = rgb_to_hex("rgb(1, 11, 111)")
print(t1)
