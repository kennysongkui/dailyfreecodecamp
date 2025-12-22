'''
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	1.00 USD
EUR	1.10 USD
GBP	1.25 USD
JPY	0.0070 USD
CAD	0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

'''

def buy_items(funds, items):

    code_dict = {
        "EUR" : 1.10,
        "GBP": 1.25,
        "JPY": 0.0070,
        "CAD": 0.75
    }

    total, code = funds
    total = float(total)
    if code != "USD":
        total = code_dict[code] * total

    print(total, code)
    x = 0
    for i in range(len(items)):
        item_price, item_code = items[i]
        item_price = float(item_price)
        if item_code != "USD":
            item_price = code_dict[item_code] * item_price
        # print(item_price, total)
        print(total - item_price)
        if total - item_price > 0:
            x += 1
            total = total - item_price
        else:
            break

    print(x)
    if x >= len(items):
        result = "Buy them all!"
    else:
        result = "Buy the first {} items.".format(x)


    print(result)
    funds = result

    return funds

# t = buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]])
# print(t)

t1 = buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]])
print(t1)