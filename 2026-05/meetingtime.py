'''
Meeting Time
Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one hour free. If no such time exists, return "None".

Each person's availability is an array of [start, end] integer pairs in 24-hour time. For example, [10, 12] would mean the person is available from 10 to 12. Start times range from 0-23, and end times range from 1-24.
For example, given:

[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]
Return 11, the start of their first shared free hour.
'''

def get_meeting_time(availability):

    common = [True] * 24
    for person  in availability:
        print(person)
        covered = [False] *24
        for start, end in person:
            for t in range(start, end):
                if t < 24:
                    covered[t] = True
        common = [common[i] and covered[i] for i in range(24)]

    print(common)
    for t in range(24):
        if common[t]:
            return t
    return 'None'


# t = get_meeting_time([[[10, 12], [15, 16]], [[11, 14], [15, 16]]])
# print(t)

t1 = get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]])
print(t1)