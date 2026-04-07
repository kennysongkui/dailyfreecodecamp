'''
Coffee Roast Detector
Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.

The given string will contain the following characters, each representing a type of bean:

An apostrophe (') is a light roast bean worth 1 point each.
A dash (-) is a medium roast bean worth 2 points each.
A period (.) is a dark roast bean worth 3 points each.
The roast level is determined by the average of all the beans.

Return:

"Light" if the average is less than 1.75.
"Medium" if the average is 1.75 to 2.5.
"Dark" if the average is greater than 2.5.
'''

def detect_roast(beans):

    n =len(beans)
    grid = list(beans)
    total_point = 0
    for i in grid:
        if i == "'":
            total_point += 1
        elif i == "-":
            total_point += 2
        elif i == ".":
            total_point += 3
        else:
            pass

    roast_level = total_point / n
    result = None
    if roast_level < 1.75:
        result = "Light"
    elif roast_level >= 1.75 and roast_level <= 2.5:
        result = "Medium"
    else:
        result = "Dark"

    beans = result
    print(result)
    return beans

# t = detect_roast("''-''''''-'-''--''''")
# print(t)

t1 = detect_roast(".--.-..-......----.'")
print(t1)