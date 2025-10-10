'''
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
'''

import datetime
def moon_phase(date_string):
    date_start = datetime.datetime(2000, 1, 6)
    date_list = date_string.split('-')
    date_end = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    days = (date_end - date_start).days
    moon_day = days % 28

    if moon_day < 7:
        date_string = "New"
    elif moon_day >= 7 and moon_day <= 14:
        date_string = "Waxing"
    elif moon_day > 14 and moon_day <=21:
        date_string = "Full"
    else:
        date_string = "Waning"

    print(moon_day)
    return date_string

# t = moon_phase("2000-01-13")
# print(t)
#
# t1 = moon_phase("2022-12-14")
# print(t1)

t2 = moon_phase("2000-01-13")
print(t2)