'''
2026 Winter Games Day 8: Luge
Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

Segment 1: 320 meters
Segment 2: 280 meters
Segment 3: 350 meters
Segment 4: 300 meters
Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.

To calculate the speed (in meters per second) for a segment, divide the distance by the time.

Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred.
'''

def get_fastest_speed(times):

    lap_distance = [320, 280, 350, 300, 250]
    x = 0
    y = 1
    for i in range(len(times)):
        speed = lap_distance[i] / times[i]
        if speed > x:
            x = speed
            y = i
    print(x, y)
    result = "The luger's fastest speed was {} m/s on segment {}.".format('%.2f'%x, y +1)

    print(result)


    times = result
    return times

t = get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128])
print(t)