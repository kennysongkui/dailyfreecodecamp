'''
Summer Solstice
Today is the summer solstice, the longest day of the year in the Northern Hemisphere and the shortest in the Southern. Given a latitude, return a string representing daytime and nighttime hours.

The latitude will be between 90 (north pole) and -90 (south pole), inclusive
The number of daytime hours = 12 + (latitude / 90) * 12
Round the daytime hours to the nearest even number
Return a 24-character string using "☀️" for daytime hours and "🌑" for nighttime hours, where:

Each character represents one hour, starting at midnight (hour 0)
Sunrise and sunset fall symmetrically around noon
For example, a latitude of 0 (the equator) has 12 hours of daylight, so sunrise is at 6:00 AM and sunset is at 6:00 PM. Return: "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑".

'''

def get_daytime_hours(latitude):
    day_hours = 12 + (latitude / 90) * 12
    half = round(day_hours /2)
    day_hours_rounded = 2 * half

    start = 12 - half
    end = 12+half -1

    chars = []
    for hour in range(24):
        if start <= hour <= end:
            chars.append("☀️")
        else:
            chars.append("🌑")
    result = ''.join(chars)
    print(result)
    latitude = result

    return latitude

t = get_daytime_hours(0)
print(t)