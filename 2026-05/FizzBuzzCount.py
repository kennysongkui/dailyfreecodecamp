'''
FizzBuzz Count
Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).

Numbers divisible by 3 count as a fizz.
Numbers divisible by 5 count as a buzz.
Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
Return an object or dictionary with the counts in the format: { fizz, buzz }.
'''


def fizz_buzz_count(start, end):
    result = {
        'fizz': 0,
        'buzz': 0,
    }
    i = start
    while i <= end:
        if i % 3 == 0 and i % 5 == 0:
            result['fizz'] += 1
            result['buzz'] += 1
            # continue
        elif i % 3 == 0:
            result['fizz'] += 1
        elif i % 5 == 0:
            result['buzz'] += 1
            print(i)
        else:
            pass
        i += 1
    print(result)

    start = result
    return start


# t = fizz_buzz_count(1, 11)
# print(t)

# t1 = fizz_buzz_count(14, 41)
# print(t1)

t2 = fizz_buzz_count(24, 100)
print(t2)