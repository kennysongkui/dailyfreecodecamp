'''
Hidden Treasure
Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".

If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
'''

def dive(map, coordinates):

    # rep_dict ={'-': "Empty", 'O':'Recovered','X':'Found'}
    # new_map = map[:]
    # x,y = coordinates
    # print(new_map[x][y])
    # report = rep_dict[new_map[x][y]]
    # print(report)
    # map = report

    x,y = coordinates
    report = ""
    if map[x][y] != "O":
        return "Empty"

    map[x][y] = "X"
    is_ok = any("O" in x for x in map)
    if is_ok:
        report = "Found"
    else:
        report = "Recovered"

    print(report)
    map = report
    return map


# t = dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1])
# print(t)
#
# t1 = dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])
# print(t1)

t2 = dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])
print(t2)

t3 =  dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2])
print(t3)