'''
Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).
'''


def is_valid_hex(s):
    source_digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
    source_abc = [ 'a', 'b', 'c', 'd', 'e', 'f']

    new_list = list(s)
    print(new_list)
    print(len(new_list))

    if len(new_list) != 4 and len(new_list) != 7:
        return False

    s = new_list.pop(0)
    print(s)
    if s != "#":
        return False
    for i in new_list:
        print(i)
        if i.isalpha():
            if i.lower() not in source_abc:
                print(i)
                return False
        else:
            if i not in source_digital:
                print(i + 1)
                return False

    result = True
    s = result

    print(new_list)

    return s


t = is_valid_hex("#123")
print(t)
