'''
Business Day Count
Given a start date and an end date, return the number of business days between the two.

Given dates are in the format "YYYY-MM-DD".
Weekdays are business days (Monday through Friday).
Weekends are not business days (Saturday and Sunday).
Include both the start and end dates when counting.
'''

from datetime import datetime, timedelta

def count_business_days(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()

    if start_date > end_date:
        start_date, end_date = end_date, start_date
    count = 0
    current = start_date

    while current <= end_date:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)
          
    print(count)

    start = count
    return start


t = count_business_days("2026-02-24", "2026-02-26")
print(t)