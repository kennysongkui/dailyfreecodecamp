'''
Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].


'''

import re

def calculate_tips(meal_price, custom_tip):
    price = float(re.sub(r'\$', '', meal_price))
    first_price = format(price * 0.15, '.2f')
    first_price = "$" + str(first_price)

    second_price = format(price * 0.20, '.2f')
    second_price = "$" + str(second_price)

    custom = float(custom_tip.strip('%')) /100

    third_price = format(price * custom, '.2f')
    third_price = "$" + str(third_price)
    print(first_price)
    # second_price = meal_price * 0.20
    # third_price = meal_price * custom_tip
    meal_price = [first_price, second_price, third_price]

    return meal_price

t = calculate_tips("$10.00", "25%")
print(t)