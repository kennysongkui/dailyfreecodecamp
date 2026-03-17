'''
2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

A snowboarder's stance is either "Regular" or "Goofy".
Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".


'''


def get_landing_stance(start_stance, rotation):

    test = (abs(rotation) // 180) % 2
    print(test)

    if test == 0:
        return start_stance

    if start_stance == "Regular":
        return "Goofy"
    else:
        return "Regular"

    return start_stance


t = get_landing_stance("Regular", 90)
print(t)
