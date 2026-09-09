'''
Birthday Countdown
Given today's date and a birthday, return the number of days until the person's next birthday.

Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
If today is their birthday, return the number of days until their next birthday (not 0).
Leap years should be accounted for.
'''

from datetime import date


def days_until_birthday(today, birthday):
    today_year, today_month, today_day = map(int, today.split('-'))
    today_str = date(today_year, today_month, today_day)
    print(today_str)
    birth_month, birth_day = map(int, birthday.split('/'))

    def is_leap(year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def next_leap_year(year):
        y = year + 1
        while not is_leap(y):
            y += 1
        return y

    if birth_month == 2 and birth_day == 29:
        if is_leap(today_year):
            this_year_bday = date(today_year, 2, 29)
            if today_str == this_year_bday:
                target_year = next_leap_year(today_year)
                target = date(target_year, 2, 29)
            elif today_str < this_year_bday:
                target = this_year_bday
            else:
                target_year = next_leap_year(today_year)
                target = date(target_year, 2, 29)
        return (target - today_str).days

    try:
        this_year_bday = date(today_year, birth_month, birth_day)
    except ValueError:
        raise

    if today_str == this_year_bday:
        target = date(today_year + 1, birth_month, birth_day)

    elif today_str < this_year_bday:
        target = this_year_bday
    else:
        target = date(today_year + 1, birth_month, birth_day)
    print(target)

    result = (target - today_str).days
    print(result)
    today = result
    return today


# t = days_until_birthday("2026-07-16", "9/7")
# print(t)

t1 = days_until_birthday("2024-03-01", "2/29")
print(t1)

t2 = days_until_birthday("2096-03-01", "2/29")
print(t2)
