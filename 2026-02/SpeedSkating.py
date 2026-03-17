'''
2026 Winter Games Day 7: Speed Skating
Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, the second to lap 2, and so on.
'''


def largest_difference(skater1, skater2):
    lap = len(skater1)
    result = 0
    lap_first = 0
    for i in range(lap):
        if skater1[i] > skater2[i]:
            j = skater1[i] - skater2[i]
        else:
            j = skater2[i] - skater1[i]
        print(j)
        if j > lap_first:
            lap_first = j
            result = i
            print(result)


    print(lap_first, result)

    skater1 = result +1
    return skater1

#
t = largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30])
print(t)

# t1 = largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23])
# print(t1)
