'''
Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).
'''
import sys
import re


def is_spam(number):
    new_arr = number.split()
    flag = False
    country_code = new_arr[0][1:]
    area_code = new_arr[1][1:4]
    # print(type(country_code))
    # print(type(country_code[0]))
    # print(area_code)
    local_code = country_code + area_code + (new_arr[2][0:3]) + new_arr[2][4:]
    # print(local_code)
    if len(country_code) > 2 or country_code[0] != "0":
        '''
        The country code is greater than 2 digits long or doesn't begin with a zero (0).
        '''
        flag = True
        number = flag
        return number
        sys.exit()
    if int(area_code) > 900 or int(area_code) < 200:
        '''
        The area code is greater than 900 or less than 200.
        '''
        flag = True
        number = flag
        return number
        sys.exit()
    sum = 0
    for i in list(new_arr[2][0:3]):
        sum += int(i)
    # print(sum)
    if str(sum) in new_arr[2][4:]:
        flag = True
        number = flag
        return number
        sys.exit()

    regex_pattern = r'(.)\1{3,10}'
    match = re.search(regex_pattern, local_code)
    if match:
        flag = True
        number = flag
        return number
        sys.exit()
    number = flag
    return number


t = is_spam("+0 (200) 234-0182")
print(t)

t1 = is_spam("+0 (555) 564-1987")
print(t1)
