'''
Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format "1 in X".

The number of dice will be between 1 and 6.
The target sum is always achievable with the given number of dice.
Round "X" to the nearest whole number.
'''


def get_odds(dice, target):
    total = 6 ** dice

    dp = [[0] * (6 * dice + 1) for _ in range(dice + 1)]
    print(total, dp)
    dp[0][0] = 1

    for i in range(1, dice + 1):
        for s in range(i, 6 * i + 1):
            ways = 0
            for d in range(1, 7):
                if s - d >= 0:
                    ways += dp[i - 1][s - d]
            dp[i][s] = ways

    count = dp[dice][target]

    rounded_x = (total + count // 2) // count
    result = f"1 in {rounded_x}"
    print(result)
    dice = result
    return dice


t = get_odds(1, 5)
print(t)
