'''
Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
'''


def generate_signature(name, title, company):
    frist = ord(name[0].upper())
    result = ''

    if frist >= 65 and frist <= 73:
        result = ">>" + name + ", " + title + " at " + company
    elif frist >= 74 and frist <= 82:
        result = "--" + name + ", " + title + " at " + company
    elif frist >= 83 and frist <= 90:
        result = "::" + name + ", " + title + " at " + company
    else:
        pass
    print(result)

    # print(ord('A'))
    # print(ord('I'))
    # print(ord('J'))
    # print(ord('R'))
    # print(ord('S'))
    # print(ord('Z'))
    name = result
    return name


t = generate_signature("Quinn Waverly", "Founder and CEO", "TechCo")
print(t)
