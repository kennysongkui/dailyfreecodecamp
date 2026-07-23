'''
Mongo ID Date
Given a MongoDB ID string, return its creation time as an ISO 8601 string.

A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.
For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z".
'''
import datetime

def mongo_id_to_date(s):

    hex_timestamp = s[0:8]
    print(hex_timestamp)
    decimal_timestamp = int(hex_timestamp, 16)
    print(decimal_timestamp)
    date_object = datetime.datetime.utcfromtimestamp(decimal_timestamp)
    print(date_object.date())

    result = date_object.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    s = result
    return s

t = mongo_id_to_date("6a094b50bcf86cd799439011")
print(t)