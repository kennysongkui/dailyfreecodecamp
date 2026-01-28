'''
Bingo! Letter
Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
'''

def get_bingo_letter(n):

    if n <= 15 :
        return "B"
    elif n <= 30:
        return "I"
    elif n <= 45:
        return "N"
    elif n <= 60:
        return "G"
    else:
        return "O"

    return n

t = get_bingo_letter(75)
print(t)