'''
2026 Winter Games Day 15: Freestyle Skiing
Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space.
Valid first words:

"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"
Valid second words:

"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"

'''


def is_valid_trick(trick_name):
    first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    second_words = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]

    first, second = trick_name.split(" ")

    if first not in first_words:
        return False
    if second not in second_words:
        return False
    result = True
    trick_name = result

    return trick_name


t = is_valid_trick("Polar Vortex")
print(t)
