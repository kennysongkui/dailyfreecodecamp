'''
Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:

Starting from the second-to-last digit, double every other digit moving left.
If doubling a digit results in a number greater than 9, subtract 9.
Sum all the digits (doubled and undoubled).
If the total is divisible by 10, the number is valid.
'''


def is_valid_card(number):
    digits = [int(ch) for ch in number if ch.isdigit()]
    print(digits)

    if len(digits) < 2:
        return False

    total = 0
    reversed_digits = digits[::-1]
    print(reversed_digits)
    for i, digit in enumerate(reversed_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit
    print(total)

    if total % 10 == 0:
        return True
    else:
        return False

    return number


t = is_valid_card("4532015112830366")
print(t)
