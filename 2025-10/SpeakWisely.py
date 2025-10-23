'''
Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."
'''

def wise_speak(sentence):

    dict_list = ["have", "must", "are", "will", "can"]

    new_list = sentence.split()
    front_list = []
    last_list = []

    for i in range(len(new_list)):
        if new_list[i] in dict_list:
            front_list = new_list[i+1:]
            last_list = new_list[:i+1]
    coma =  front_list[-1][-1]

    front_list[0] = front_list[0].capitalize()
    last_list[0] = last_list[0].lower()
    front_sent = " ".join(front_list).replace(coma, ",")
    last_sent = " ".join(last_list) + coma
    print(new_list)
    print(front_list)
    print(last_list)

    print(front_list[-1][-1])
    print(front_sent)
    print(last_sent)
    sentence = front_sent + " " + last_sent

    return sentence


t = wise_speak("You must speak wisely.")
print(t)