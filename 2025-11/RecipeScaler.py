'''
Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given.
'''


def scale_recipe(ingredients, scale):
    new_arr = []
    for i in ingredients:
        list = i.split()
        quantity = str(float(list[0]) * float(scale))
        if quantity.endswith('.0'):
            quantity = quantity[:-2]
        list[0] = quantity

        new_arr.append(" ".join(list))

    ingredients = new_arr
    return ingredients


#
# t = scale_recipe(["2 C Flour", "1.5 T Sugar"], 2.5)
# print(t)

t1 = scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5)
print(t1)
