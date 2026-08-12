'''
Zoning Regulations
Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are violating zoning rules.

Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to) 4 neighbors, horizontal or vertical, are a type it cannot be adjacent to.

Label	Type	Cannot be adjacent to
"i"	industrial	"R", "I"
"A"	Agricultural	"C"
"R"	Residential	"i", "C"
"I"	Institutional	"i"
"C"	Commercial	"R", "A"
"" (empty string)	undeveloped	no restrictions
Return the coordinates of all violating cells as an array of [row, col] pairs, in any order. If no violations exist, return an empty array.
'''


def get_zone_violations(grid):
    restrictions = {
        "i": {"R", "I"},
        "A": {"C"},
        "R": {"i", "C"},
        "I": {"i"},
        "C": {"R", "A"},
        "": set()
    }

    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])
    violations = []

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            cell_type = grid[r][c]
            forbidden = restrictions.get(cell_type, set())
            if not forbidden:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor_type = grid[nr][nc]
                    if neighbor_type in forbidden:
                        violations.append([r, c])
                        break

    print(violations)
    grid = violations

    return grid


# t = get_zone_violations([["R", "C"], ["", "C"]])
# print(t)

t1 = get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]])
print(t1)