'''
Daylight Hours
December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

Latitude	Daylight Hours
-90	24
-75	23
-60	21
-45	15
-30	13
-15	12
0	12
15	11
30	10
45	9
60	6
75	2
90	0
If the given latitude does not exactly match a table entry, use the value of the closest latitude.

'''


def daylight_hours(latitude):
    latitude_daylight_dic = {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
        0: 12,
        15: 11,
        30: 10,
        45: 9,
        60: 6,
        75: 2,
        90: 0

    }

    latitude_key = list(latitude_daylight_dic.keys())
    # print(latitude_key)
    if latitude in latitude_key:
        x = latitude_daylight_dic[latitude]
    else:
        min_difference = abs(latitude - latitude_key[0])

        for i in range(1, len(latitude_key)):
            current_difference  = abs(latitude - latitude_key[i])
            if current_difference < min_difference:
                min_difference = current_difference
                closest_index = i
        x = latitude_daylight_dic[latitude_key[closest_index]]
    # print(x)
    latitude = x
    return latitude


t = daylight_hours(45)
print(t)
