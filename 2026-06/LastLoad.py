'''
Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.

Calculate your average daily usage from the usage history and assume that amount of usage each day going forward.
'''


def last_load_date(scoops, usage):
    total = 0
    days = len(usage)

    for i in range(days):
        total += usage[i]

    ave_usage = total / days

    day = scoops // ave_usage
    print(day)
    scoops = day
    return scoops


t = last_load_date(10, [2, 2, 2, 2, 2, 2, 2])
print(t)
