'''
Name Initials
Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".


'''

def get_initials(name):

    new_arr = []
    test_arr = name.split()
    for i in test_arr:
        print(i)
        new_arr.append(i[0].upper() +".")

    print(new_arr)
    result = ''.join(new_arr)
    print(result)
    name = result
    return name

t = get_initials("Tommy Millwood")
print(t)