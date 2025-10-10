'''
Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

Return "heat" if the current temperature is below the target.
Return "cool" if the current temperature is above the target.
Return "hold" if the current temperature is equal to the target.
'''

def adjust_thermostat(temp, target):
    test = "heat"
    if (temp - target) < 0 :
        test ="heat"
    if (temp -target) > 0:
        test = "cool"
    if (temp - target) == 0:
        test = "hold"

    temp = test
    return temp

t = adjust_thermostat(-20.5, -10.1)
print(t)