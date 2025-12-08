'''
Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".
'''


def format_date(date_string):
    month_dict = {
        'December': '12',
        'November': '11',
        'October': '10',
        'September': '09',
        'August': '08',
        'July': '07',
        'June': '06',
        'May': '05',
        'April': '04',
        'March': '03',
        'February': '02',
        'January': '01'
    }
    new_arr = date_string.split()
    new_str = new_arr[2] + '-' + month_dict[new_arr[0]] + '-' + new_arr[1].rstrip(',').zfill(2)
    print(new_arr)
    print(new_arr[1].zfill(2))
    print(new_str)
    date_string = new_str
    return date_string


t = format_date("December 6, 2025")
print(t)
