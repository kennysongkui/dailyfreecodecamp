'''
Digit Rotation Escape
Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

Check rotation 0 (the given number) first.
Given numbers won't contain any zeros.
Return the first rotation number if one is found, or "none" if not.
'''

def get_rotation(n):

    new_n = str(n)
    n_len = len(new_n)
    # new_arr = list(new_n)
    for i in range(n_len):
        # print(new_n[i:])
        number_arr = new_n[i:] + new_n[:i]
        number = int(number_arr)
        # print( number)

        if number % n_len == 0:
            return i

    # print(new_n, n_len, new_arr)

    flag = "none"
    n = flag

    return n

t = get_rotation(123)
print(t)