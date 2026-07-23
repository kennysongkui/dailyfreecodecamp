'''
Pizza Party
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

Divide each person's hours worked by 3 to get their slice count.
You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
Each person gets a minimum of two slices.
Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.
'''
import math


def get_pizzas_to_order(hours_worked):
    total_slice = 0
    for i in hours_worked:
        if math.ceil(i / 3) < 2:
            total_slice += 2
        else:
            total_slice += math.ceil(i / 3)
    print(total_slice)

    total_pizzas = math.ceil(total_slice / 8)
    print(total_pizzas)
    hours_worked = total_pizzas
    return hours_worked


# t = get_pizzas_to_order([8, 8, 8])
# print(t)

t1 = get_pizzas_to_order([1, 2, 3, 4, 5])
print(t1)
