'''
Blood Type Compatibility
Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
'''

def can_donate(donor, recipient):

    donor_letter = donor[:-1]
    donor_rh = donor[-1]
    recipient_letter = recipient[:-1]
    recipient_rh = recipient[-1]

    if donor_letter == "O":
        letter_ok  = True
    elif donor_letter == "A":
        letter_ok = recipient_letter in ("A", "AB")
    elif donor_letter == "B":
        letter_ok = recipient_letter in ("B", "AB")
    elif donor_letter == "AB":
        letter_ok = recipient_letter == "AB"
    else:
        letter_ok = False

    if donor_rh == "-":
        rh_ok = True
    else:
        rh_ok = recipient_rh == "+"

    result = letter_ok and rh_ok

    donor = result

    return donor

t = can_donate("B+", "B+")
print(t)

