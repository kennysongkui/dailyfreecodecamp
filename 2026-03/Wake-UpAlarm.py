'''
Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.
'''

def alarm_check(alarm_time, wake_time):
    alarm_hour, alarm_minute = alarm_time.split(":")
    alarm_time_minute = int(alarm_hour) * 60 + int(alarm_minute)
    wake_hour, wake_minute = wake_time.split(":")
    wake_time_minute = int(wake_hour) * 60  + int(wake_minute)

    print(alarm_time_minute, wake_time_minute)

    m = wake_time_minute - alarm_time_minute

    if m < -10 :
        return "early"
    elif m > 10:
        return "late"
    else:
        return "on time"
    return alarm_time

t = alarm_check("07:00", "06:45")
print(t)