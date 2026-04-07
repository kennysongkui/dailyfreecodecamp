'''
Trail Traversal
Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right

"D" is a move down

"L" is a move left

"U" is a move up

There will always be a single continuous trail, without any branching, from your current location to your goal.

Each trail location will have a maximum of two traversable locations touching it.

For example, given:

[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
Return "RDDRDD".
'''

from collections import deque


def navigate_trail(map):
    rows = len(map)
    cols = len(map[0])

    start = goal = None

    for i in range(rows):
        for j in range(cols):
            # print(map[i][j])
            if map[i][j] == "C":
                start = (i, j)
            elif map[i][j] == "G":
                goal = (i, j)

    print(start, goal)

    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    visited = set()
    parent = {}
    queue = deque([start])
    visited.add(start)

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for dx, dy, move in directions:
            nx, ny = x+dx, y +dy
            if 0 <= nx < rows and 0 <= ny <cols and (nx, ny) not in visited:
                cell = map[nx][ny]
                if cell in ('T','G'):
                    visited.add((nx, ny))
                    parent[(nx, ny)] = ((x,y), move)
                    queue.append((nx, ny))


    path = []
    cur = goal
    while cur != start:
        prev, move = parent[cur]
        path.append(move)
        cur = prev
    path.reverse()

    result = ''.join(path)
    print(result)
    map = result

    return map


t = navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])
print(t)
