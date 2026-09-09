'''
Contrast Rating 3
Given two arrays representing RGB values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:

First, convert each RGB value to relative luminance:

Divide each channel [R, G, B] by 255 to get a value between 0 and 1
Apply the gamma correction formula to each channel:
If the channel value is less than or equal to 0.04045: channel / 12.92
Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B
Then, calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

'''


def get_contrast_rating(rgb1, rgb2, is_large_text):
    l1 = luminance(rgb1)
    l2 = luminance(rgb2)

    lighter = max(l1, l2)
    darker = min(l1, l2)
    ratio = (lighter + 0.05) / (darker + 0.05)

    if is_large_text:
        if ratio >= 4.5:
            return "AAA"
        elif ratio >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if ratio >= 7.0:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        else:
            return "Fail"

    return rgb1


def luminance(rgb):
    def gamma_correct(channle):
        c = channle / 255.0
        if c <= 0.04045:
            return c / 12.92
        else:
            return ((c + 0.055) / 1.055) ** 2.4

    r = gamma_correct(rgb[0])
    g = gamma_correct(rgb[1])
    b = gamma_correct(rgb[2])

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


t = get_contrast_rating([255, 255, 255], [0, 0, 0], False)
print(t)
