'''
Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array.
'''


def get_allergen_friendly_meals(meals, allergens):
    print(allergens)

    avoid_set = set(allergens)
    safe_meal = []

    # for i in meals:
    #     meal, allergen = i
    #     print(meal, allergen)
    #     for j in allergens:
    #
    #         if j in allergen:
    #             print(1)
    #             continue
    #         else:
    #             print(2)
    #             safe_meal.append(meal)
    print(avoid_set)
    for meal_name, allergen in meals:
        if not (set(allergen) & avoid_set):
            safe_meal.append(meal_name)

    # print(safe_meal)
    meals = safe_meal
    return meals


# t = get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"])
# print(t)

t1 = get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]],
                                  ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"])
print(t1)
