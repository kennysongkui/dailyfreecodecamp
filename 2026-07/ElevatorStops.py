'''
Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the elevator should visit them to minimize number of floors traveled.

If tied, go up first
Floors with a request must be visited when the elevator first passes them
'''


def elevator_stops(current_floor, stops):
    if not stops:
        return []

    unique_floors = set(stops)
    min_floor = min(unique_floors)
    max_floor = max(unique_floors)

    if current_floor < min_floor:
        direction = 'up'
    elif current_floor > max_floor:
        direction = 'down'
    else:
        dist_up_first = (max_floor - current_floor) + (max_floor - min_floor)
        dist_down_first = (current_floor - min_floor) + (max_floor - min_floor)
        direction = 'up' if dist_up_first <= dist_down_first else 'down'

    if direction == 'up':
        up_part = sorted([f for f in unique_floors if f >= current_floor])
        down_part = sorted([f for f in unique_floors if f < current_floor], reverse=True)
        result = up_part + down_part
    else:
        down_part = sorted([f for f in unique_floors if f <= current_floor], reverse=True)
        up_part = sorted([f for f in unique_floors if f > current_floor])
        result = down_part + up_part

    print(result)
    current_floor = result

    return current_floor


t = elevator_stops(5, [2, 8, 3, 9])
print(t)
