'''
Contrast Rating 1
Given a contrast ratio and a boolean indicating whether the text is large, return the WCAG rating using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

'''

def get_contrast_rating(ratio, is_large_text):

    if is_large_text:
        if float(ratio) >= 4.5:
            return "AAA"
        elif float(ratio) >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if float(ratio) >= 7.0:
            return "AAA"
        elif float(ratio) >= 4.5:
            return "AA"
        else:
            return "Fail"

    return ratio

t = get_contrast_rating("7.5", False)
print(t)