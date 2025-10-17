'''
String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.

'''

def count(text, parameter):
    count = 0
    str = text
    # print(str)
    while len(str) > 0:
        flag = str.find(parameter)
        # print(flag)
        if flag >= 0 :
            str = str[flag+1:]
            # print(str)
            count +=1
        else:
            break
    text = count
    return text

t = count('abcdefg', 'def')
print(t)

t1 = count('101010101010101010101', '101')
print(t1)