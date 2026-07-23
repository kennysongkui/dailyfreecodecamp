'''
Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.
'''


def get_oldest(people):
    # name = people[0]['name']
    # age = people[0]['age']
    # print(type(age))
    #
    # for i in range(1, len(people)):
    #     # print(type(item['age']))
    #     if people[i]['age'] > age:
    #         age = people[i]['age']
    #         name = people[i]['name']
    #     else:
    #         continue
    #
    # print(name)
    # result = [name]

    max_age = max(person['age'] for person in people)
    result = [person['name'] for person in people if person['age'] == max_age]
    print(result)
    people = result
    return people


# t = get_oldest([{"name": "Brenda", "age": 40}])
# print(t)

t1 = get_oldest([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}])
print(t1)
