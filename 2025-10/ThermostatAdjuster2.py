'''
Thermostat Adjuster 2
Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
Return "Hold" if the current temperature is equal to the target.
To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).


'''

def adjust_thermostat(current_f, target_c):
    target_f = (float(target_c) * 1.8) + 32
    current_f = float(current_f)
    result = ""
    if current_f - target_f > 0:
        degres = format((current_f - target_f), '.1f')
        result = "Cool: {} degrees Fahrenheit".format(degres)
    elif current_f - target_f == 0:
        result = "Hold"
    else:
        degree = format((target_f - current_f), '.1f')
        result = "Heat: {} degrees Fahrenheit".format(degree)

    current_f = result
    print(target_f)
    return current_f

t = adjust_thermostat(32, 0)
print(t)

t1 = adjust_thermostat(72, 18)
print(t1)