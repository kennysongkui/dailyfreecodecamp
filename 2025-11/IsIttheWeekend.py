'''
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.
'''


def days_until_weekend(date_string):
    # week_dict = {
    #     0: "Sunday",
    #     1: "Monday",
    #     2: "Tuesday",
    #     3: "Wednesday",
    #     4: "Thursday",
    #     5: "Friday",
    #     6: "Saturday"
    # }
    year, month, day = date_string.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    if (month == 1 or month == 2):
        year -= 1
        month += 12
    c = int(year / 100)
    y = int(year - c * 100)
    print(c, y, month)
    week = y + int(y / 4) + int(c / 4) - 2 * c + int(26 * (month + 1) / 10) + day - 1
    print(week)
    while week < 0:
        week += 7
    week %= 7
    print(week)
    day = 6 - week
    print(day)
    result = ""
    if day == 1:
        result = "1 day until the weekend."
    elif day > 1 and day < 6:
        result = str(day) + " days until the weekend."
    else:
        result = "It's the weekend!"

    print(result)
    date_string = result
    return date_string


# t = days_until_weekend("2025-11-14")
# print(t)

t1 = days_until_weekend("2025-01-01")
print(t1)