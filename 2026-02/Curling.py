'''
2026 Winter Games Day 16: Curling
Given a 5x5 matrix representing the "house" at the end of a curling round, determine which team scores and how many points they score.

The layout:

The center cell (index [2, 2]) is the "button".
The 8 cells directly surrounding the button represent ring 1.
And the 16 cells on the outer edge of the house represent ring 2.
In the given matrix:

"." represents an empty space.
"R" represents a space with a red stone.
"Y" represents a space with a yellow stone.
Scoring rules:

Only one team can score per round.
The team with the stone closest to the button scores.
The scoring team earns 1 point for each of their stones that is closer to the button than the opponent's closest stone.
The lower the ring number, the closer to the center the stone is.
If both teams' closest stone is the same distance from the center, no team scores.
Return:

A string in the format "team: number_of_points". e.g: "R: 2".
or "No points awarded" if neither team scored any points.
For example, given:

[
  [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", "R", ".", ".", "."],
  [".", ".", ".", ".", "."]
]
Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows closest.
'''


def score_curling(house):
    '''
    first_cycle = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
    first_score_red = 0
    first_score_yellow = 0
    second_score_red = 0
    second_score_yellow = 0

    for i in range(5):
        for j in range(5):
            if (i, j) in first_cycle:
                if house[i][j] == "R":
                    first_score_red += 1
                if house[i][j] == "Y":
                    first_score_yellow += 1
            else:
                if house[i][j] == "R":
                    second_score_red += 1
                if house[i][j] == "Y":
                    second_score_yellow += 1
    print(first_score_red, first_score_yellow, second_score_red, second_score_yellow)
    '''

    red_rings = []
    yellow_rings = []

    for r in range(5):
        for c in range(5):
            cell = house[r][c]
            if cell == "R" or cell == "Y":
                ring = max(abs(r - 2), abs(c - 2))
                if cell == "R":
                    red_rings.append(ring)
                else:
                    yellow_rings.append(ring)

    print(red_rings, yellow_rings)
    INF = 3
    min_red = min(red_rings) if red_rings else INF
    min_yellow = min(yellow_rings) if yellow_rings else INF

    if min_red == min_yellow:
        return "No points awarded"
    if min_red < min_yellow:
        count = sum(1 for r in red_rings if r < min_yellow)
        return f"R: {count}"
    else:
        count = sum(1 for y in yellow_rings if y < min_red)
        return f"Y: {count}"

    return house


t = score_curling(
    [[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."],
     [".", ".", ".", ".", "."]])
print(t)

t1 = score_curling(
    [[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."],
     [".", "Y", "R", "R", "."]])
print(t1)
