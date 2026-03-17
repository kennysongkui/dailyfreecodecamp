'''
Letter and Number Count
Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.
Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".
'''

def count_letters_and_numbers(s):
    new_arr = list(s)
    count_l = 0
    count_n = 0

    for i in new_arr:
        if i.isdigit():
            count_n += 1
        elif i.isalpha():
            count_l += 1
        else:
            pass

    if count_l == 1 and count_n ==1:
        result = f"The string has 1 letter and 1 number."
    else:
        result = f"The string has {count_l} letters and {count_n} numbers."
    print(result)
    s = result
    return s

# t = count_letters_and_numbers("helloworld123")
# print(t)

t1 = count_letters_and_numbers("A1!")
print(t1)
