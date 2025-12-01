'''
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.
'''

def get_next_location(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    pre_location = None
    now_location = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                pre_location = (i,j)
            elif matrix[i][j] == 2:
                now_location = (i, j)

    print(pre_location, now_location)

    dr = now_location[0] - pre_location[0]
    dc = now_location[1] - pre_location[1]
    next_row = now_location[0] + dr
    next_col = now_location[1] + dc

    bounce_dr = dr
    bounce_dc = dc
    print(next_row, next_col, bounce_dc, bounce_dr)
    if next_row < 0 or next_row >= rows:
        bounce_dr = -dr

    if next_col < 0 or next_col >= cols:
        bounce_dc = -dc

    final_row = now_location[0] + bounce_dr
    final_col = now_location[1] + bounce_dc

    finnal_location = [final_row, final_col]
    print(finnal_location)
    matrix = finnal_location
    return matrix

t = get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]])
print(t)