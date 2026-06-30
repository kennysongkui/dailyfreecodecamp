'''
Unique Stair Climber
Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.
'''


def get_unique_climbs(steps):
    if steps <= 1:
        return 1

    prev2, prev1 = 1, 1
    for i in range(2, steps + 1):

        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
        print(curr, prev2, prev1)

    # print(prev1, curr, prev2)
    result = prev1

    steps = result
    return steps


t = get_unique_climbs(18)
print(t)
