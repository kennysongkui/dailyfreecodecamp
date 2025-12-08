'''
Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".
'''


def convert_to_kgs(lbs):
    kilo = float(lbs) * 0.453592

    if lbs == 1:
        message = str(lbs) + " pound equals "+ f"{kilo:.2f}" +" kilograms."
        return message
    # print(f"{kilo:.2f}")
    if  f"{kilo:.2f}"== "1.00":
        message = str(lbs) + " pounds equals " + f"{kilo:.2f}" + " kilogram."
        return message

    message = str(lbs) + " pounds equals "+ f"{kilo:.2f}" +" kilograms."

    # print(kilo)
    # print(message)
    lbs = message
    return lbs


# t = convert_to_kgs(100)
# print(t)

t1 = convert_to_kgs(2.20462)
print(t1)