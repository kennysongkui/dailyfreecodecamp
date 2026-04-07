'''
Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds".

'''

def get_milestone(years):
    milestones = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    # 如果没有达到第一个里程碑（1 年），返回 Newlyweds
    if years < 1:
        return "Newlyweds"

    # 找到所有小于等于当前年限的里程碑年份
    # 由于 years >= 1，且字典最小键为 1，所以这里至少会有一个匹配项
    valid_milestones = [y for y in milestones.keys() if years >= y]

    # 返回最大的那个里程碑名称（即最近达到的里程碑）
    max_year = max(valid_milestones)

    result = milestones[max_year]
    print(result)
    years = result
    return years

t = get_milestone(0)
print(t)