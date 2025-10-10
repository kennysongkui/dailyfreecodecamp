'''
Fill The Tank
Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

tankSize is the total capacity of the tank in gallons.
fuelLevel is the current amount of fuel in the tank in gallons.
pricePerGallon is the cost of one gallon of fuel.
The returned value should be rounded to two decimal places in the format: "$d.dd".
'''


def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    total = (tank_size - fuel_level) * price_per_gallon
    dollar_sign = chr(36)
    tank_size = dollar_sign + f"{total:.2f}"
    return tank_size


t = cost_to_fill(20, 0, 4.00)
print(t)