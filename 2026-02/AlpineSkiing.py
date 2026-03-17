'''
2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25
'''


def get_hill_rating(drop, distance, hill_type):
    dict_hill_type = {
        'Downhill': 1.2,
        'Slalom': 0.9,
        'Giant Slalom': 1.0
    }

    i = (drop / distance) * dict_hill_type[hill_type]

    print(i)
    if i < 0.1:
        return "Green"
    elif i >= 0.1 and i <= 0.25:
        return "Blue"
    else:
        return "Black"

    return drop


t = get_hill_rating(95, 900, "Slalom")
print(t)
