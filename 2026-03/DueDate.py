'''
Due Date
Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month.
'''


def get_due_date(date_str):
    year, month, day = date_str.split("-")
    print(year, month, day)

    new_month = int(month) + 9
    print(new_month)

    if new_month <= 12:
        pass
    else:
        new_month = new_month - 12
        year = int(year) + 1
    print(year, new_month)

    if new_month == 2 and int(day) >28:
        day = 28
    else:
        pass

    result = f"{year}-{new_month:02}-{day}"

    print(result)

    date_str = result
    return date_str


t = get_due_date("2025-03-30")
print(t)
