'''
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.
'''

def convert_to_km(miles):
    kilometer = miles * 1.60934
    print(kilometer)
    result = '{:.2f}'.format(kilometer)
    result = result.rstrip('0')
    result = result.rstrip('.')
    # result1 = round(kilometer,2)
    # print(result, result1)
    miles = float(result)
    return miles

t = convert_to_km(1)
print(t)
