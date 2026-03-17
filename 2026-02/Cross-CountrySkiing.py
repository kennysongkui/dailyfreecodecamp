'''
2026 Winter Games Day 5: Cross-Country Skiing
Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

Given times are strings in "H:MM:SS" format.
Given times will be in order from fastest to slowest.
The winners time (fastest time) should correspond to "0".
Each other time should show the time behind the winner, in the format "+M:SS".
For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].
'''


def get_relative_results(results):
    # new_arr = ["0",]
    # first = results[0]
    # first_h, first_M, first_S = first.split(":")
    # for i in range(1,len(results)):
    #     h, M, S = results[i].split(":")
    #     if S < first_S :
    #         first_M = int(first_M) - 1
    #         S =  60  + int(S) - int(first_M)
    #         print(S)

    def to_seconds(t):
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s

    if not results:
        return []

    winner_sec = to_seconds(results[0])
    result = ["0"]

    for i in results[1:]:
        diff = to_seconds(i) - winner_sec
        minutes = diff // 60
        seconds = diff % 60
        result.append(f"+{minutes}:{seconds:02d}")

    results = result

    return results


t = get_relative_results(["1:25:32", "1:26:10", "1:27:05"])
print(t)
