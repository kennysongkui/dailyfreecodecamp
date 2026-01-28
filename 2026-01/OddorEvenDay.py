'''
Odd or Even Day
Given a timestamp (number of milliseconds since the Unix epoch), return:

"odd" if the day of the month for that timestamp is odd.
"even" if the day of the month for that timestamp is even.
For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.
'''

from datetime import datetime, timezone

def odd_or_even_day(timestamp):
    # print(type(timestamp), timestamp)

    # test = datetime.datetime.now()
    # print(type(test), test)
    dt_object = datetime.fromtimestamp(timestamp/1000, tz=timezone.utc)
    day = dt_object.strftime("%d")
    print(day)

    if int(day) % 2 == 0:
        return "even"
    else:
        return "odd"
    return timestamp

# t = odd_or_even_day(1769472000000)
# print(t)

t1 = odd_or_even_day(1769444440000)
print(t1)

t2 = odd_or_even_day(6739456780000)
print(t2)
