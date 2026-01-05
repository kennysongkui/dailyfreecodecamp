'''
Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.
'''
import math


def fuel_to_add(current_gallons, required_liters):
    required_gallons = math.ceil(required_liters / 3.78541)
    print(required_gallons)
    result = required_gallons - current_gallons

    if result < 0:
        result = 0
    print(result)
    current_gallons = result
    return current_gallons


# t = fuel_to_add(0, 1)
# print(t)
#
# t1 = fuel_to_add(5, 40)
# print(t1)

t2 = fuel_to_add(10, 30)
print(t2)
