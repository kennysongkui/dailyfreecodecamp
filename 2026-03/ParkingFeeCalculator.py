'''
Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.
'''

from math import ceil


def calculate_parking_fee(park_time, pickup_time):
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    park_time_min = to_minutes(park_time)
    pickup_time_min = to_minutes(pickup_time)

    if pickup_time_min > park_time_min:
        total_minutes = pickup_time_min - park_time_min
        overnight = False
    else:
        total_minutes = (24 * 60 - park_time_min) + pickup_time_min
        overnight = True

    hours = ceil(total_minutes / 60)
    fee = hours * 3
    if overnight:
        fee += 10

    if fee < 5:
        fee = 5

    result = "${}".format(fee)
    print(result)
    park_time = result

    return park_time

#
# t = calculate_parking_fee("09:00", "11:00")
# print(t)

t1 = calculate_parking_fee("18:15", "01:30")
print(t1)
