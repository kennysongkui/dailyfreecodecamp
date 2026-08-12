'''
Jet Lagged
Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.

The given cities will be from the following list that includes their UTC offset:

City	Offset
"Los Angeles"	-8
"New York"	-5
"London"	0
"Istanbul"	+3
"Dubai"	+4
"Hong Kong"	+8
"Tokyo"	+9
To calculate jet lag hours:

Find the timezone difference in hours between the two cities.
Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier
Return the jet lag hours rounded to one decimal place.
'''


def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):
    offsets = {
        "Los Angeles": -8,
        "New York": -5,
        "London": 0,
        "Istanbul": 3,
        "Dubai": 4,
        "Hong Kong": 8,
        "Tokyo": 9
    }

    timezone_diff = abs(offsets[arrival_city] - offsets[departure_city])
    print(timezone_diff)

    multiplier = 1.5 if direction.lower() == "east" else 1.0

    jet_lag_hours = timezone_diff + (flight_duration * 0.1) * multiplier

    result = round(jet_lag_hours, 1)
    print(result)
    departure_city = result

    return departure_city


t = get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east")
print(t)
