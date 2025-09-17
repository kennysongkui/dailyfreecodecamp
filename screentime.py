
'''
Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.
'''
def too_much_screen_time(hours):
    week_time = hours
    # print(week_time)
    flag = False
    # print(flag)

    for i in week_time:
        if i >= 10:
            flag = True

    if sum(week_time) / 7 >= 6:
        flag = True

    # print(flag)
    for i in range(len(week_time) - 2):
        if ((week_time[i] + week_time[i + 1] + week_time[i + 2]) / 3) >= 8:
            flag = True

    hours = flag

    return hours

#
# t = too_much_screen_time([1, 2, 3, 4, 5, 6, 7])
# print(t)
#
# t1 =too_much_screen_time([7, 8, 8, 4, 2, 2, 3])
# print(t1)
t2 = too_much_screen_time([3, 9, 4, 8, 5, 7, 6])
print(t2)
