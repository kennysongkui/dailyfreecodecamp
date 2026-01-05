'''
Resolution Streak
Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

The first sub-array is day 1, and second day 2, and so on.
A day is considered successful if all three of the following goals are met:

You walked at least 10,000 steps.
You had no more than 120 minutes of screen time.
You read at least five pages.
If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful days.

If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.
'''


def resolution_streak(days):
    user_status = {
        'streak_days': 0,
        'on_failed': 0,
        'failed_days': 0
    }

    for i in range(len(days)):
        steps, screen_time, read_page = days[i]
        if steps < 10000 or screen_time > 120 or read_page < 5:
            user_status['failed_days'] += 1
            if user_status['on_failed'] == 0:
                user_status['on_failed'] = i + 1
        else:
            user_status['streak_days'] += 1

    print(user_status['streak_days'], user_status['on_failed'], user_status['failed_days'])
    if user_status['on_failed'] > 0:
        result = "Resolution failed on day {}: {} day streak.".format(user_status['on_failed'],
                                                                      user_status['failed_days'])
    else:
        result = "Resolution on track: {} day streak.".format(user_status['streak_days'])
    print(result)

    days = result
    return days


# t = resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]])
# print(t)

t1 = resolution_streak([[10000, 120, 5], [10950, 121, 11]])
print(t1)
