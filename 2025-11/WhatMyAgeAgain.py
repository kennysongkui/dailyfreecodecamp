'''
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.
'''


def calculate_age(birthday):
    year, month, day = birthday.split('-')
    if int(month) < 11:
        age = 2025 - int(year)
    elif int(month) == 11:
        if int(day) <= 27:
            age = 2025 - int(year)
    else:
        age = 2025 - int(year) - 1

    print(year, month, day)
    print(age)
    birthday = age
    return birthday


# t = calculate_age("2000-11-20")
# print(t)
t1 = calculate_age("2000-12-01")
print(t1)
