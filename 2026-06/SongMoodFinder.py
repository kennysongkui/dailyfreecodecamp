'''
Song Mood Finder
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood	Genre	BPM Range
"focus"	"classical"	60–109
"focus"	"electronic"	60–89
"happy"	"pop"	60–180
"happy"	"classical"	110–180
"happy"	"rock"	60–129
"happy"	"electronic"	90–134
"hype"	"rock"	130–180
"hype"	"electronic"	135–180

'''


def get_mood(genre, bpm):
    if genre == "classical":
        if 60 <= bpm <= 109:
            return "focus"
        elif 110 <= bpm <= 180:
            return "happy"
    elif genre == "electronic":
        if 60 <= bpm <= 89:
            return "focus"
        elif 90 <= bpm <= 134:
            return "happy"
        elif 135 <= bpm <= 180:
            return "hype"
    elif genre == "rock":
        if 60 <= bpm <= 129:
            return "happy"
        elif 130 <= bpm <= 180:
            return "hype"
    elif genre == "pop":
        if 60 <= bpm <= 109:
            return "happy"

    return ""


t = get_mood("rock", 111)
print(t)
