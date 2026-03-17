'''
2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200
'''


def get_difficulty(track):
    # new_arr = list(track)
    # print(new_arr)

    total = 0
    n = len(track)

    for i in range(n - 1):
        if track[i] in 'LR' and track[i + 1] in 'LR' and track[i] != track[i + 1]:
            total += 15
    for i in range(n - 1):
        if track[i] == "S" and track[i + 1] in 'LR' and track[i] != track[i + 1]:
            total += 5
    for i in range(n):
        if track[i] in 'LR':
            part_of_change = False
            if i > 0 and track[i - 1] in 'LR' and track[i - 1] != track[i]:
                part_of_change = True
            if i < n - 1 and track[i + 1] in 'LR' and track[i + 1] != track[i]:
                part_of_change = True
            if not part_of_change:
                total += 5


    print(total)
    if total <= 100:
        return "Easy"
    elif total <= 200:
        return "Medium"
    else:
        return "Hard"

    return track


# t = get_difficulty("SLSLLSRRLSRLRL")
# print(t)

t1 = get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS")
print(t1)
