'''
Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed.

'''


def send_message(route):
    arr = route
    gap_satellite_time = (len(arr) - 1) * 0.5
    sum = 0
    for i in arr:
        sum += i
    pass_through_time = (sum / 300000)
    total_time = format((gap_satellite_time + pass_through_time), '.4f')
    # route = str(format((gap_satellite_time + pass_through_time), '.4f')).rstrip('0')
    route = float(str(total_time).rstrip('0')) # 返回值不能位字符串，需要是浮点数
    return route



t = send_message([300000, 300000])
print(t)

t1 = send_message([1000000, 500000000, 1000000])
print(t1)

t2 = send_message([802101, 725994, 112808, 3625770, 481239])
print(t2)
