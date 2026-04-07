'''
Element Size
Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
'''


def get_element_size(window_size, element_vw, element_vh):
    width, height = window_size.split("x")
    print(width, height)
    vw = element_vw[:-2]
    vh = element_vh[:-2]
    print(vw, vh)

    re_width = int(int(width) * int(vw) / 100)
    re_height = int(int(height) * int(vh) / 100)

    result = "{} x {}".format(re_width, re_height)
    print(result)
    window_size = result
    return window_size


t = get_element_size("1200 x 800", "50vw", "50vh")
print(t)
