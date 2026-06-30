'''
Hidden Key
Welcome to the 250th daily challenge!

Given an encoded string, decode it using an encryption key and return it.

To find the key:

Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.
To decode the message, go over each letter in the encoded message and:

Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
Shift the encoded letter backward in the alphabet by that number.
If the shift goes before "A", wrap around to "Z".
For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to decode the full message.

Only letters are shifted, spaces are returned as-is.
All given and returned letters are uppercase.
'''



def decode(message):
    key = "VLHCGMDLNHVL"
    key_len = len(key)
    print(key_len)
    result = []
    flag = 0
    # key = 'V'
    for i, ch in enumerate(message):

        if ch == ' ':
            result.append(' ')
            flag -= 1
            continue
        if not ch.isalpha():
            result.append(ch)
            flag -= 1
            continue
        print(i, flag)
        # if i > key_len:
        #     i -= key_len
        key_char = key[(i + flag) % key_len]
        # key_char = key[i%key_len]
        print(key_char)
        shift = ord(key_char) - ord('A') + 1
        # print(shift)
        original_ord = ord(ch) - shift
        if original_ord < ord('A'):
            original_ord += 26
        result.append(chr(original_ord))

    print(result)

    message = ''.join(result)

    print(14%12)

    return message


# t = decode("YAVJYNXE")
# print(t)

# t1 = decode("YALLUT PQUMJP")
# print(t1)

t2 = decode("UAC DYR EISAKYM")
print(t2)

# t3 = decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB")
# print(t3)