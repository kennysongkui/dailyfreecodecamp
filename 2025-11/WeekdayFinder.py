'''
Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
'''


def get_weekday(date_string):
    week_dict = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    year, month, day = date_string.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    if (month == 1 or month == 2):
        year -= 1
        month += 12
    c = int(year / 100)
    y = int(year - c * 100)
    print(c,y, month)
    week = y + int(y / 4) + int(c / 4) - 2 * c + int(26 * (month + 1) / 10) + day - 1
    print(week)
    while week < 0:
        week += 7
    week %= 7
    print(week)
    date_string = week_dict[week]

    print(year, month, day)

    return date_string


t = get_weekday("1999-12-31")
print(t)

t1 = get_weekday("2025-11-06")
print(t1)
