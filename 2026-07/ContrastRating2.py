'''
Contrast Rating 2
Given two relative luminance values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:

Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

'''

def get_contrast_rating(l1, l2, is_large_text):

    ratio = (l1+0.05)/(l2+0.05)
    print(ratio)

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

    return l1

t = get_contrast_rating(1.0, 0.0, False)
print(t)