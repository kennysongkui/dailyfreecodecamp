'''
Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.
'''


def truncate_text(text):
    s_len = len(text)
    result = None

    if s_len > 20:
        result = text[:17] + "..."
    else:
        result = text
    # s = text
    # print(s[:17] + "...")
    text = result
    return text


# t = truncate_text("Hello, world!")
# print(t)

t1 = truncate_text("This string should get truncated.")
print(t1)
