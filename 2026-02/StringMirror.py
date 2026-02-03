'''
String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.
'''

def mirror(s):

    t = s[::-1]
    result = s + t
    print(result)
    s = result
    return s

t = mirror("freeCodeCamp")
print(t)