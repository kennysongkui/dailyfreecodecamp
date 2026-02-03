'''
Letters-Numbers
Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
'''


def separate_letters_and_numbers(s):
    new_arr = [s[0]]
    for i in range(1, len(s)):
        current = s[i]
        prev = s[i - 1]

        current_is_digit = current.isdigit()
        prev_is_digit = prev.isdigit()

        if current_is_digit != prev_is_digit:
            new_arr.append("-")

        new_arr.append(current)
    result = "".join(new_arr)

    print(new_arr, result)
    s = result

    return s


t = separate_letters_and_numbers("ABC123")
print(t)
