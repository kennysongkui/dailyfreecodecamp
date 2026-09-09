'''
Tally Counter
Given a string of tally marks, return the total count represented.

Each pipe "|" represents one count.
Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
Groups are separated by a space.

'''

def get_tally_count(s):
    count = s.count('|') + s.count('/')
    print(count)
    s = count
    return s

t = get_tally_count("||||")
print(t)