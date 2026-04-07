'''
Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.

'''


def get_movie_night_cost(day, showtime, number_of_tickets):
    total = 0
    time_part = showtime[:-2]
    meridiem = showtime[-2:]

    if day == "Tuesday":
        total = number_of_tickets * 5
        return f"${total:.2f}"

    if day in ("Friday", "Saturday", "Sunday"):
        base_price = 12.00
    else:
        base_price = 10.00

    hour_str, minute_str = time_part.split(":")
    hour = int(hour_str)
    minute = int(minute_str)

    if meridiem == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    if hour < 17:
        price_per_ticket = base_price - 2.00
    else:
        price_per_ticket = base_price

    total = number_of_tickets * price_per_ticket

    result = f"${total:.2f}"
    # print(result)
    day = str(result)
    return day


t = get_movie_night_cost("Saturday", "10:00pm", 1)
print(t)
