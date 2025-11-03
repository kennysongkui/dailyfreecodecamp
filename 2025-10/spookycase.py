'''
SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.
'''

def spookify(boo):
    new_str = ""
    flag = True
    for i in boo:

        if i == "_" or i == "-":
            i  = "~"
            new_str += i
            continue

        if flag :
            new_str += i.upper()
            flag = False
        else:
            new_str += i.lower()
            flag = True
    print(new_str)
    boo = new_str

    return boo

t = spookify("hello_world")
print(t)