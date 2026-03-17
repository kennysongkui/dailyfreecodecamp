'''
2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.
'''

def compute_score(judge_scores, *penalties):
    test_arr = sorted(judge_scores)
    new_arr = test_arr[1:-1]
    print(new_arr)
    total = 0
    for i in new_arr:
        total += i
    print(total)

    for j in penalties:
        total -= j

    print(total)
    judge_scores = total

    return judge_scores

t = compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1)
print(t)