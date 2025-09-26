'''
Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].
'''

def speeding(speeds, limit):
    new_arr = []
    count = 0
    sum = 0

    for i in range(len(speeds)):
        if speeds[i] > limit:
            print(count)
            count += 1
            sum += (speeds[i] - limit)

    print(count)
    if count != 0 :
        avg = sum / count
    else:
        avg = 0

    new_arr.append(count)
    new_arr.append(avg)
    speeds = new_arr[:]

    return speeds

# t = speeding([50, 60, 55], 60)
# print(t)

t1 = speeding([61, 81, 74, 88, 65, 71, 68], 70)
print(t1)