'''
Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
'''


def count_rectangles(width, height):
    total_width = width * (width + 1) // 2
    total_height = height * (height + 1) // 2
    print(total_width, total_height)
    result = total_width * total_height
    width = result
    return width


t = count_rectangles(5, 4)
print(t)
