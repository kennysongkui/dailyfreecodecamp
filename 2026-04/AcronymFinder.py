'''
Acronym Finder
Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

"National Avocado Storage Authority"
"Cats Infiltration Agency"
"Fluffy Beanbag Inspectors"
"Department Of Jelly"
"Wild Honey Organization"
"Eating Pancakes Administration"
Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.
'''

def find_org(acronym):

    test_dict = {
        "NASA":"National Avocado Storage Authority",
        "CIA":"Cats Infiltration Agency",
        "FBI":"Fluffy Beanbag Inspectors",
        "DOJ":"Department Of Jelly",
        "WHO":"Wild Honey Organization",
        "EPA":"Eating Pancakes Administration"
    }

    for i in test_dict.keys():
        if acronym == i :
            result = test_dict[i]
        else:
            pass
    print(result)
    acronym = result
    return acronym

t = find_org("NASA")
print(t)