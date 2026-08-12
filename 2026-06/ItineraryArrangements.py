'''
Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.

The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional stops can be placed anywhere in the itinerary, subject to the following rules:

"breakfast" is always first, with at least one stop before "lunch".
"lunch" must appear before "dinner", with at least one stop in between.
At most, one optional stop may appear after "dinner".
Return the number of valid arrangements.

'''


def get_itinerary_count(stops):
    n = len(stops)

    if n < 2:
        return 0

    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    result = factorial * (2 * n - 3)
    print(result)
    stops = result
    return stops


t = get_itinerary_count(["library", "park"])
print(t)
