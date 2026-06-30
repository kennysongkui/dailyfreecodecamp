'''
What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
'''

from datetime import datetime
def get_day_of_week(timestamp):

    # print(type(timestamp))
    # day_week_dict = {
    #     0
    #     1: ""
    # }
    dt_object = datetime.utcfromtimestamp(timestamp/1000.0)
    day_of_week = dt_object.strftime("%A")
    # print(dt_object.strftime('%A'))
    # day_of_week = dt_object.weekday()
    # print(day_of_week)
    timestamp = day_of_week
    return timestamp

t = get_day_of_week(1773576000000)
print(t)