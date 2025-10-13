'''
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
'''


def to_12(time):
    new_arr = list(time)
    front_two = int(new_arr[0] + new_arr[1])
    new_front_two  = 0
    mide_two = new_arr[2] + new_arr[3]
    last_two = "AM"
    if front_two == 0:
        new_front_two = 12
    else:
        new_front_two = front_two

    if front_two - 12 >= 0:
        last_two = "PM"
        new_front_two = front_two -12



    time = "{}:{} {}".format(new_front_two,mide_two,last_two)
    print(new_front_two)
    return time

#
# t = to_12("2324")
# print(t)

t1 = to_12("0030")
print(t1)