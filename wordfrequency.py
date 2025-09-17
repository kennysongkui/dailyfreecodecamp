'''
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
'''
def get_words(paragraph):
    s = paragraph.lower().split()
    y = []
    for i in s:
        e = i.maketrans("","",",.!")
        f = i.translate(e)
        y.append(f)

    count_dist = dict()
    for i in y :
        if i in count_dist:
            count_dist[i] += 1
        else:
            count_dist[i] = 1
    test = sorted(count_dist.items(),key = lambda asd:asd[1],reverse=True)[:3]
    test1 =[]
    for i in test :
        key, value = i
        test1.append(key)
    paragraph = test1
    return paragraph

test = get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
print(test)

test1 = get_words("I like coding. I like testing. I love debugging!")
# print(test1)
test2 = get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")
print(test2)
