'''
Good Day
Given a time string in "HH:MM" format (24-hour clock), return:

"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59
'''


def get_greeting(s):
    hour = int(s[:2])
    print(hour)

    if hour >= 5 and hour < 12:
        return "Good morning"
    elif hour >= 12 and hour < 18:
        return "Good afternoon"
    elif hour >= 18 and hour < 22:
        return "Good evening"
    else:
        return "Good night"
    return s


t = get_greeting("06:30")
print(t)
