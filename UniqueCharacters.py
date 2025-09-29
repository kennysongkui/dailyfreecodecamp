'''
Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.

'''

def all_unique(s):
    arr = list(s)
    test = s
    print(arr)
    for i in range(len(arr)):
        if test.count(arr[i]) > 1 :
            s = False
            break
        s = True

    return s

t = all_unique("QwErTy123!@")
print(t)