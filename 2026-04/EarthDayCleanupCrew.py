'''
Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	Base Value
"bottle"	10
"can"	6
"bag"	8
"tire"	35
"straw"	4
"cardboard"	3
"newspaper"	3
"shoe"	12
"electronics"	25
"battery"	18
"mattress"	38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.
Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.
'''


def get_cleanup_score(items):
    base_values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    total_score = 0
    prev_item = None
    streak = 0
    item_number = 0

    for i in items:

        item_number += 1

        if isinstance(i, list) and len(i) == 2 and i[0] == "rare":
            value = i[1]

            prev_item = None
            streak = 0
        else:

            if i not in base_values:
                raise ValueError(f"找不到物品：{i}")
            base = base_values[i]

            if i == prev_item:
                streak += 1
            else:
                streak = 1
                prev_item = i
            value = base + (streak - 1)

        if item_number % 5 == 0:
            multiplier = item_number // 5 + 1
        else:
            multiplier = 1

        total_score += value * multiplier
        print(i)

    print(total_score)
    items = total_score
    return items


t = get_cleanup_score(["bottle", "straw", "shoe", "battery"])
print(t)
