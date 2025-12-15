'''
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
'''

def title_case(title):
    new_list = title.split()
    str_list =[]
    for i in new_list:
        i = i.lower()
        i = i.capitalize()
        print(i.capitalize())
        str_list.append(i)
    print(new_list)
    print(str_list)
    title = ' '.join(str_list)
    return title

t = title_case("hello world")
print(t)