'''
Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

*
 *
*
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 **
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

'''

def generate_snowflake(crystals):
    new_arr = crystals.split("\n")
    print(new_arr)
    test_arr = []
    for i in new_arr:
        i = i + i[::-1]
        print(i)
        test_arr.append(i)
    print(test_arr)
    crystals = "\n".join(test_arr)
    return crystals

t = generate_snowflake("* \n *\n* ")
print(t)

t1 = generate_snowflake("X=~")
print(t1)