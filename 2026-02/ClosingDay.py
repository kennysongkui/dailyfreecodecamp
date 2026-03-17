'''
2026 Winter Games Day 17: Closing Day
Given a 2D array of medal winners, return a medal count for each country as a CSV string.

In the given array, each sub-array represents a single event: [gold_winner, silver_winner, bronze_winner]

The returned CSV string should have the following format, with the first line being headers:

Country,Gold,Silver,Bronze,Total
country_name,gold_count,silver_count,bronze_count,total_medals
Separate new lines with the new line character ("\n").
Do not include spaces around commas or at the end of lines.
Sort the returned CSV by gold medal count, highest first. If two countries have the same gold medal count, sort the tied ones alphabetically.
For example, given:

[
  ["USA", "CAN", "NOR"],
  ["NOR", "USA", "CAN"],
  ["USA", "NOR", "SWE"]
]
Return:

"Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
Which looks like this when printed:

Country,Gold,Silver,Bronze,Total
USA,2,1,0,3
NOR,1,1,1,3
CAN,0,1,1,2
SWE,0,0,1,1
'''


def count_medals(winners):
    from collections import defaultdict

    counts = defaultdict(lambda: {"gold": 0, "silver": 0, "bronze": 0})
    for gold, silver, bronze in winners:
        counts[gold]["gold"] += 1
        counts[silver]["silver"] += 1
        counts[bronze]["bronze"] += 1
    # print(counts)

    table = []
    for country, medals in counts.items():
        # print(country, medals)
        g = medals["gold"]
        s = medals["silver"]
        b = medals["bronze"]
        total = g + s + b
        table.append((country, g, s, b, total))

    table.sort(key=lambda x: (-x[1], x[0]))

    lines = ["Country, Gold, Silver, Bronze, Total"]
    for country, g, s, b, t in table:
        lines.append(f"{country},{g},{s},{b},{t}")

    print(lines)

    result = f"\\n".join(lines)
    print(result)

    winners = result

    return winners


t = count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]])
print(t)
