'''
2026 Winter Games Day 11: Ice Hockey
Given an array of 6 ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.

Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L". Where:
"W" is the number of wins in regulation, worth 3 points each
"OTW" is the number of overtime wins, worth 2 points each
"OTL" is the number of overtime losses, worth 1 point each
"L" is the number of losses, worth 0 points each
For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.

Find the total number of points for each team and return "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be FIN vs SWE and CAN vs USA."
'''


def get_semifinal_matchups(teams):
    team_record = []
    for i in teams:
        country, point_item = i.split(":")
        w, otw, otl, l = map(int, point_item.split("-"))

        points = w * 3 + otw * 2 + otl * 1 + l * 0

        team_record.append((country, points))

    team_record.sort(key=lambda x: x[1], reverse=True)

    print(team_record)

    first = team_record[0][0]
    second = team_record[1][0]
    third = team_record[2][0]
    fourth = team_record[3][0]

    result = "The semi-final games will be {} vs {} and {} vs {}.".format(first, fourth, second, third)
    teams = result

    print(result)
    return teams


t = get_semifinal_matchups(
    ["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"])
print(t)
