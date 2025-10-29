'''
Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
'''


def format(seconds):
    # H = seconds // 3600
    # t = seconds % 3600
    # M = "{:02d}".format(t // 60)
    # S = "{:02d}".format(t % 60)
    #
    # print(H)
    # print(t)
    # print(M)
    # print(S)
    if seconds >= 3600:
        H = seconds // 3600
        t = seconds % 3600
        M = "{:02d}".format(t // 60)
        S = "{:02d}".format(t % 60)
        report = "{}:{}:{}".format(H, M, S)
    elif seconds >= 60 and seconds < 3600:
        M = seconds // 60
        S = "{:02d}".format(seconds % 60)
        report = "{}:{}".format(M, S)
    else:
        M = 0
        S = S = "{:02d}".format(seconds)
        report = "{}:{}".format(M, S)
    print(report)

    seconds = report
    return seconds


# t = format(99999)
# print(t)
#
# t1 = format(5555)
# print(t1)

# t2 = format(1)
# print(t2)

t3 = format(500)
print(t3)