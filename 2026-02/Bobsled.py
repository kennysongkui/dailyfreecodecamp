'''
2026 Winter Games Day 12: Bobsled
Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by itself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements.
'''


def check_eligibility(athlete_weights, sled_weight):
    sled_weight_item = [[1, 162, 247], [2, 170, 390], [4, 210, 630]]
    count = len(athlete_weights)
    sum_athlete = 0
    for j in athlete_weights:
        sum_athlete += j
    print(sum_athlete)
    for i in sled_weight_item:
        print(i)
        if i[0] == count:
            if sled_weight < i[1]:
                return "Not Eligible"
            if sum_athlete + sled_weight > i[2]:
                return "Not Eligible"
    result = "Eligible"

    athlete_weights = result

    return athlete_weights


# t = check_eligibility([78], 165)
# print(t)

t1 = check_eligibility([80], 170)
print(t1)
