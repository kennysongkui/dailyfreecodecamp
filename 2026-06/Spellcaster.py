'''
Spellcaster
Given a string of spell codes you are casting, calculate the total score.

Each character in the string represents a spell:

Code	Spell	Category	Base Score
"f"	Fire	Destruction	3
"l"	Lightning	Destruction	3
"i"	Ice	Control	2
"w"	Wind	Control	2
"h"	Heal	Restoration	1
"s"	Shield	Restoration	1
A combo multiplier is applied based on how many spells in a row have been cast from different categories:

The first spell always scores at base value.
Each consecutive spell from a different category than the previous increases the multiplier by 1.
Casting a spell from the same category as the previous resets the multiplier back to 1.
The score for each spell is its base score multiplied by the current multiplier.
Return the total score from the sequence of spells.
'''


def cast(spells):
    spell_info = {
        'f': ('Destruction', 3),
        'l': ('Destruction', 3),
        'i': ('Control', 2),
        'w': ('Control', 2),
        'h': ('Restoration', 1),
        's': ('Restoration', 1),
    }

    if not spells:
        return 0

    total = 0
    prev_category = None
    multiplier = 1

    for ch in spells:
        category, base = spell_info[ch]

        if prev_category is None:
            multiplier = 1
        elif category == prev_category:
            multiplier = 1
        else:
            multiplier += 1
        total += base * multiplier
        prev_category = category

    print(total)
    spells = total
    return spells


t = cast("fihwl")
print(t)
