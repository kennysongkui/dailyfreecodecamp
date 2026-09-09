'''
Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

You may only sell after you buy.
You may perform at most one buy and one sell transaction. Once you sell, you cannot buy again.
You can only buy whole shares.
Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

'''


def get_max_profit(prices, budget):
    price_cents = [int(round(p * 100)) for p in prices]
    print(price_cents)
    budget_cents = int(round(budget * 100))
    n = len(price_cents)

    if n < 2:
        return "0.00"

    suffix_max = [0] * n
    suffix_max[-1] = price_cents[-1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(price_cents[i], suffix_max[i + 1])

    max_profit_cents = 0

    for i in range(n - 1):
        buy = price_cents[i]
        if buy == 0:
            continue

        shares = budget_cents // buy
        if shares <= 0:
            continue
        sell = suffix_max[i + 1]
        if sell > buy:
            profit = shares * (sell - buy)
            if profit > max_profit_cents:
                max_profit_cents = profit
    dollars = max_profit_cents // 100
    cents = max_profit_cents % 100
    result = f"{dollars}.{cents:02d}"

    prices = result
    return prices


t = get_max_profit([5, 6], 50)
print(t)
