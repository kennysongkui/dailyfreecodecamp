'''
Passing Exam Count
Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
'''

def passing_count(scores, passing_score):

    count_passed = 0

    for i in scores:
        if i >= passing_score:
            count_passed += 1

    print(count_passed)
    scores = count_passed
    return scores


t = passing_count([90, 85, 75, 60, 50], 70)
print(t)