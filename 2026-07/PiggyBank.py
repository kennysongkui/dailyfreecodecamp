'''
Piggy Bank
Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".

The object may contain any of the following:

Coin	Value
pennies	$0.01
nickels	$0.05
dimes	$0.10
quarters	$0.25

'''


def piggy_bank(coins):
    if not coins:
        return "$0.00"
    coin_value = {
        "pennies": 0.01,
        "nickels": 0.05,
        "dimes": 0.10,
        "quarters": 0.25
    }

    total = 0.00
    for item in coins:
        total += coin_value[item] * coins[item]
        print(item)

    print(total)

    result = f"${round(total, 2)}"
    print(result)
    coins = result
    return coins


# t = piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6})
# print(t)

# t1 = piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1})
# print(t1)

t2 = piggy_bank({})
print(t2)
