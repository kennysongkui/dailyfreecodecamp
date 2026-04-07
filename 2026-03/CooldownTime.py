'''
Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
'''

from datetime import datetime


def can_retake(finish_time, current_time):
    fmt = "%Y-%m-%dT%H:%M:%S"
    t1 = datetime.strptime(finish_time, fmt)
    t2 = datetime.strptime(current_time, fmt)
    delta = t2 - t1
    print(delta.total_seconds())

    if delta.total_seconds() >= 48 * 3600:
        return True
    else:
        return False

    return finish_time


t = can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")
print(t)
