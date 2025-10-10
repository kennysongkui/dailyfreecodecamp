'''
CSV Header Parser
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
'''

def get_headings(csv):
    new_arr = csv.split(",")
    arr = []
    for i in new_arr:
        print(i)
        e =i.strip()
        print(e)
        arr.append(e)
        # i.rstrip()
        # print(i)

    csv = arr[:]
    return csv

t = get_headings("name,age,city")
print(t)

t1 = get_headings("username , email , signup date ")
print(t1)