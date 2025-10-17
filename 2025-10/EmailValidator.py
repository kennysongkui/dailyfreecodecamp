'''
Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
'''
import re


def validate(email):

    new_list = email.split('@')

    if len(new_list) != 2:
        email = False
        return email
    if re.match(r'^[a-zA-Z0-9_.-]+', new_list[0]) :
        if new_list[0][0] == "." or new_list[0][-1] == ".":
            email = False
            return email

    domain_list = new_list[1].split('.')
    print(domain_list)
    if len(domain_list) >= 2:
        print("0")
        print(domain_list[-1])
        if "" in domain_list:
            email = False
            return email
        if len(domain_list[-1]) < 2 :
            email = False
            return email
            print("1")
        elif re.search(r'\d', domain_list[-1]):
            print("2")
            email = False
            return email
    else:
        email = False


    email = True
    return email


# t = validate("a@b.cd")
# print(t)
#
# t1 = validate(".b@sh.rc")
# print(t1)
#
# t2 = validate("develop.ment_user@c0D!NG.R.CKS")
# print(t2)
#
# t3 = validate("hello@world..com")
# print(t3)

t4 = validate("example@test.c0")
print(t4)