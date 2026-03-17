'''
2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.

Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:

165.5
172.0
158.0
180.0
169.5
175.0
162.0
170.0
If your score is the best, return "Gold"
If it's second best, return "Silver"
If it's third best, return "Bronze"
Otherwise, return "No Medal"
'''


def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    point_list = sorted([165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0])

    self_point = distance_points + style_points + wind_comp + k_point_bonus
    print(self_point)
    print(point_list)
    result = None
    if self_point > point_list[-1]:
        return "Gold"
    elif self_point > point_list[-2]:
        return "Silver"
    elif self_point > point_list[-3]:
        return "Bronze"
    else:
        return "No Medal"

    return distance_points


t = ski_jump_medal(125.0, 58.0, 0.0, 6.0)
print(t)
