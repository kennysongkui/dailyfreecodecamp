'''
Sleep Debt
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.

Include tonight's hours in the total time needed to catch up.
If you've slept enough to cover tonight's target or more, return 0.
'''

def sleep_debt(hours_slept, target_hours):
    sum = target_hours
    for i in hours_slept:
        sum += (target_hours - i)
    print(sum)
    if sum < 0 :
        sum = 0
    hours_slept = sum

    return hours_slept

# t = sleep_debt([6, 6, 6, 6, 6, 6], 8)
# print(t)

t1 = sleep_debt([8, 9, 10, 9, 10, 7], 7)
print(t1)