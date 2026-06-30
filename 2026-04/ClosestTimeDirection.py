'''
Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

Times are given in 24-hour format ("HH:MM")
The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:

"forward" if moving forward is shorter
"backward" if moving backward is shorter
"equal" if both directions take the same amount of time

'''


def get_direction(time1, time2):
    def total_min(time):
        hour, minitue = time.split(":")
        total = int(hour) * 60 + int(minitue)

        return total

    time1_min = total_min(time1)
    time2_min = total_min(time2)
    print(time1_min, time2_min)

    total_minutes = 24 * 60

    if time2_min >= time1_min:
        forward = time2_min - time1_min
    else:
        forward = (total_minutes - time1_min) + time2_min

    backward = total_minutes - forward

    if forward < backward:
        return "forward"
    elif backward < forward:
        return "backward"
    else:
        return "equal"

    return time1


# t = get_direction("10:00", "12:00")
# print(t)

t1 = get_direction("11:00", "05:00")
print(t1)

t2 = get_direction("15:45", "01:10")
print(t2)
