'''
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.
'''


def is_valid_message(message, validation):
    new_arr = message.split()
    val_len = len(validation)
    result = True
    if len(new_arr) != val_len:
        # result = False
        # message = result
        # return message
        return False
    for i in range(val_len):
        if validation[i].lower() not in new_arr[i].lower():
            return False
    message = result
    return message


t = is_valid_message("hello world", "hw")
print(t)

t1 = is_valid_message("Coding challenge are boring.", "cca")
print(t1)

t2 = is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD")
print(t2)