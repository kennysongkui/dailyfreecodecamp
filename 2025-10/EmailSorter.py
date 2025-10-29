'''
Email Sorter
On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].
'''

def sort(emails):
    new_arr = []
    for i in emails:
        x, y =i.split('@')
        dict = {}
        dict["username"] = x
        dict['domainname'] = y
        new_arr.append(dict)

    result = sorted(new_arr, key=lambda x: (x['domainname'].lower(), x['username'].lower()))
    # result1 = sorted(result, key=lambda x: x['username'].lower())
    # print(result)
    # print(result1)
    test_arr = []
    for j in result:
        x = j['username']
        y = j['domainname']
        test = x +'@'+y
        test_arr.append(test)
    # print(test_arr)
    emails = test_arr
    return emails


t = sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"])
print(t)

t1 = sort(["user@z.com", "user@y.com", "user@x.com"])
print(t1)

t2 = sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"])
print(t2)

