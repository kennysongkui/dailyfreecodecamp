'''
Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height ratio.

The given strings will be in the format "WxH", for example, "1920x1080".
The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces to "16:9".
Return a string in format "W:H", for example, "16:9".
'''

import math


def get_wider_aspect_ratio(a, b):
    w1, h1 = map(int, a.split('x'))
    w2, h2 = map(int, b.split('x'))

    if w1 * h2 > w2 * h1:
        w, h = w1, h1
    else:
        w, h = w2, h2

    g = math.gcd(w, h)
    result = f"{w // g}:{h // g}"
    print(result)
    a = result
    return a


t = get_wider_aspect_ratio("1920x1080", "800x600")
print(t)
