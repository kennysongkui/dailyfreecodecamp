'''
Streaming Cost
Given an array representing movies in the cart of your streaming service, and a string for your subscription tier, return the total cost of the movies.

Each item in the cart is an object with a "format" ("HD" or "4K") and a "type" ("rent" or "buy"). Their costs are:

"rent"	"buy"
"HD"	$3.99	$12.99
"4K"	$5.99	$19.99
Apply the following subscription tier discounts:

"none": full price
"basic": 10% off
"premium": 25% off
Return the total cost rounded to two decimal places in the format "$D.CC".
'''


def get_streaming_bill(cart, subscription):
    price_table = {
        ("HD", "rent"): 3.99,
        ("HD", "buy"): 12.99,
        ("4K", "rent"): 5.99,
        ("4K", "buy"): 19.99
    }

    discount_map = {
        'none': 1.0,
        'basic': 0.9,
        'premium': 0.75
    }

    total = 0.0
    for item in cart:
        fmt = item["format"]
        typ = item["type"]
        total += price_table[(fmt, typ)]

    total *= discount_map[subscription]
    total_rounded = round(total, 2)
    result = f"${total_rounded:.2f}"
    print(result)
    cart = result

    return cart


t = get_streaming_bill([{"format": "HD", "type": "rent"}], "none")
print(t)
