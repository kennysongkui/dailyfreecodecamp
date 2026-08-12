'''
British to American
Given a sentence, convert any British English spellings to their American English equivalents using the following lookup table and return the updated sentence:

British	American
"colour"	"color"
"flavour"	"flavor"
"honour"	"honor"
"neighbour"	"neighbor"
"labour"	"labor"
"humour"	"humor"
"centre"	"center"
"fibre"	"fiber"
"defence"	"defense"
"offence"	"offense"
"organise"	"organize"
"recognise"	"recognize"
"analyse"	"analyze"
Replacements should be case-insensitive. For example, "Colour" should become "Color".
The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For example, "colouring" should become "coloring", and "disorganised" should become "disorganized".
'''
import re


def british_to_american(sentence):
    BRITISH_TO_AMERICAN = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze"
    }

    def _convert_case(british_word, american_word):
        if british_word.isupper():
            return american_word.upper()
        if british_word[0].isupper() and british_word[1:].islower():
            return american_word.capitalize()
        return american_word.lower()

    patterns = sorted(BRITISH_TO_AMERICAN.keys(), key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, patterns)), re.IGNORECASE)

    def replace(match: re.Match):
        brit = match.group(0)
        amer = BRITISH_TO_AMERICAN[brit.lower()]
        return _convert_case(brit, amer)

    result = regex.sub(replace, sentence)
    print(result)

    sentence = result

    return sentence


t = british_to_american("I love the colour blue.")
print(t)
