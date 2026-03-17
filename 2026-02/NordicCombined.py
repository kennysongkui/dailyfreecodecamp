'''
2026 Winter Games Day 13: Nordic Combined
Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of the Nordic Combined.

The athlete with the highest jump score starts first (0 second delay). All other athletes start later based on how far behind their jump score is compared to the best jump.

To calculate the delay for each athlete, subtract the athlete's jump score from the best overall jump score and multiply the result by 1.5. Round the delay up to the nearest integer.
'''

import math


def calculate_start_delays(jump_scores):
    result = []
    max_scores = max(jump_scores)
    for i in jump_scores:
        source = math.ceil((max_scores - i) * 1.5)
        result.append(source)

    print(result)
    jump_scores = result
    return jump_scores


t = calculate_start_delays([120, 110, 125])
print(t)
