'''
HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.
'''

import re
def extract_attributes(element):
    # pattern = re.compile(r'<(.*?)>')
    # new_list = pattern.search(element).group(1)
    # print(new_list)
    # new_arr = []
    # for i in range(len(new_list)):
    #     print(new_list[i])
    #     if re.search(r'=', new_list[i]):
    #         new_arr.append(new_list[i])
    # print(new_arr)
    # result_arr = []
    # for j in new_arr:
    #     test = re.sub(r'=', ", ", j)
    #     result_arr.append(re.sub(r'"',"", test))
    #
    # element = result_arr[:]

    pattern = r'(\w+)="([^"]*)"'
    matches = re.findall(pattern, element)
    new_arr = []
    for attr, value in matches:
        test = attr +", " + value
        new_arr.append(test)
    element = new_arr[:]
    print(matches)
    return element

# t = extract_attributes('<span class="red"></span>')
# print(t)

# t1 = extract_attributes('<input name="email" type="email" required="true" />')
# print(t1)

t2 = extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>')
print(t2)