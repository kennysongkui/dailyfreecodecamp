'''
Coffee Order Parser
Given a string for a coffee order, identify any menu items and return a formatted order.

Use the following menu items and prices:

Item	Price
"cold brew"	$4.50
"oat latte"	$5.00
"cappuccino"	$4.75
"espresso"	$3.00
"vanilla syrup"	$0.75
"caramel drizzle"	$0.60
"extra shot"	$0.50
"oat milk"	$0.75
"cream"	$0.75
Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.

For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"

Items should appear in the order they appear in the menu and the total price should always have two decimal places.
'''


def format_coffee_order(order):
    menu = [
        ("cold brew", 4.50),
        ("oat latte", 5.00),
        ("cappuccino", 4.75),
        ("espresso", 3.00),
        ("vanilla syrup", 0.75),
        ("caramel drizzle", 0.60),
        ("extra shot", 0.50),
        ("oat milk", 0.75),
        ("cream", 0.75),
    ]

    matched_items = []
    total = 0.0

    for item, price in menu:
        if item in order:
            matched_items.append(item)
            total += price

            print(item, price)

    if not matched_items:
        return ""

    items_str = " + ".join(matched_items)

    result = f"{items_str}: ${total:.2f}"
    print(result)
    order = result
    return order


t = format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.")
print(t)
