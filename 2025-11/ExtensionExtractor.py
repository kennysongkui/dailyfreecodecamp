'''
Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.
'''

def get_extension(filename):
    new_str = ''.join(reversed(filename))
    index = 0
    for i in new_str:
        if i == ".":
            index = new_str.index(i)
            break
    print(index)
    if index > 0 :
        result = ''.join(reversed(new_str[:index]))
    else:
        result = "none"
    print(result)

    print(new_str)
    filename = result
    return filename


# t = get_extension("document.txt")
# print(t)
#
# t1 = get_extension(".gitignore")
# print(t1)

# t2 = get_extension("README")
# print(t2)

t3 = get_extension("final.draft.")
print(t3)