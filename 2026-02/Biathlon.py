'''
2026 Winter Games Day 3: Biathlon
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.
'''

def calculate_penalty_distance(rounds):
    total = 0
    for i in rounds:
        total += (5-i) * 150

    rounds = total
    print(total)
    return rounds

t = calculate_penalty_distance([5, 5])
print(t)