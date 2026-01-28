'''
Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

The input string is in the format "WxH". For example, "800x600".
The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format.
'''


def scale_image(size, scale):
    x, y = size.split("x")
    print(x, y)
    print(type(x))

    result = str(round(int(x) * scale)) + "x" + str(round(int(y) * scale))
    print(result)
    size = result
    return size


# t = scale_image("800x600", 2)
# print(t)

t1 = scale_image("1024x768", 0.5)
print(t1)

t2 = scale_image("300x200", 1.5)
print(t2)
