'''
Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late fees.

Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
The rental tier is the number of days before the rental is due back: 1, 3, or 7.
Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked out at any time on March 15 is due back by 12:00 PM UTC on March 16.
Each day past the due date and time incurs a late fee.
Pricing is as follows:

Tier	Base cost	Late fee per day
1 day	$4.99	$3.99
3 days	$3.99	$2.99
7 days	$2.99	$0.99
Return the total cost rounded to two decimal places in the format "$D.CC".
'''

from datetime import datetime, timedelta, time, timezone
import math


def get_rental_cost(rented, returned, tier):
    pricing = {
        1: {"base": 4.99, "late": 3.99},
        3: {"base": 3.99, "late": 2.99},
        7: {"base": 2.99, "late": 0.99}
    }

    rental_dt = datetime.fromisoformat(rented.replace('Z', '+00:00'))
    print(rental_dt)
    return_dt = datetime.fromisoformat(returned.replace('Z', '+00:00'))

    start_date = rental_dt.date()
    print(start_date)
    due_date = start_date + timedelta(days=tier)
    due_time = datetime.combine(due_date, time(12, 0, 0), tzinfo=timezone.utc)
    print(due_date, due_time)

    late_days = 0
    if return_dt > due_time:
        delta = return_dt - due_time
        late_days = math.ceil(delta.total_seconds() / (24 * 3600))

    base_cost = pricing[tier]["base"]
    late_fee = pricing[tier]["late"] * late_days
    total = base_cost + late_fee

    total_rounded = round(total, 2)
    result = f"${total_rounded:.2f}"
    print(result)

    rented = result

    return rented


t = get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1)
print(t)
