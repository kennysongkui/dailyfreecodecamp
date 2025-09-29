'''
IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed.
'''
import re


def is_valid_ipv4(ipv4):
    arr = ipv4.split(".")
    if len(arr) != 4:
        ipv4 = False
    print(arr)
    for i in arr:
        print(i)
        match = re.match(r"^0\d+", i)
        if match:
            ipv4 = False
            break
        if len(i) ==0:
            ipv4 = False
            break

        if int(i) >= 0 and int(i) <= 255:
            print(i)
            ipv4 = True
        else:
            ipv4 = False
            break
    return ipv4


# t = is_valid_ipv4("192.168.01.1")
# print(t)
# t1 = is_valid_ipv4("256.101.50.115")
# print(t1)
t2 = is_valid_ipv4("192.168.101.")
print(t2)
