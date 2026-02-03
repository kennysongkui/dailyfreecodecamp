'''
Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.
'''

from datetime import datetime, timedelta

def digital_detox(logs):

    if not logs:
        return True

    datetime_logs = []
    for log in logs:
        try:
            dt = datetime.strptime(log, "%Y-%m-%d %H:%M:%S")
            datetime_logs.append(dt)
        except ValueError:
            continue

    datetime_logs.sort()

    for i in range(len(datetime_logs)):
        for j in range(i+1, len(datetime_logs)):
            time_diff = datetime_logs[j] - datetime_logs[i]
            if time_diff.total_seconds() <= 4 * 3600:
                return False
            else:
                break

    daily_counts = {}
    for dt in datetime_logs:
        date_str = dt.strftime("%Y-%m-%d")
        daily_counts[date_str] = daily_counts.get(date_str, 0) +1

        if daily_counts[date_str] > 2:
            return False

    result = True
    logs = result


    return logs

t = digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])
print(t)