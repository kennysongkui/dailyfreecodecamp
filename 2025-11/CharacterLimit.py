'''
Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.
'''

def can_post(message):
    # str_list = message.split()
    # str_len = 0
    # for i in str_list:
    #     str_len += len(i)
    #     print(str_len)
    # # print(str_len)
    #
    str_len = len(message)

    if str_len < 40:
        flag = "short post"
    elif str_len >=40 and str_len < 80:
        flag = "long post"
    else:
        flag = "invalid post"

    print(flag)
    message = flag
    return message


# t = can_post("This is a longer message but still under eighty characters.")
# print(t)

t1 = can_post("This message is too long to fit into either of the character limits for a social media post.")
print(t1)