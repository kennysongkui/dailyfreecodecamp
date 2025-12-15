'''
Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

'''

def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph * 1.60934
    result = None
    if speed_kph <= speed_limit_kph :
        result = "Not Speeding"
    elif speed_kph > speed_limit_kph and speed_kph <= speed_limit_kph + 5:
        result = "Warning"
    else:
        result = "Ticket"

    print(result)
    speed_mph = result

    return speed_mph

t = speed_check(30, 70)
print(t)