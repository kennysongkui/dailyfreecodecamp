'''
Horoscope Match
Given two star sign strings, return their compatibility percentage.

The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries" after "Pisces". Find the shortest distance between the two signs and return the compatibility:

Distance	Compatibility
0	"100%"
1	"40%"
2	"80%"
3	"30%"
4	"90%"
5	"20%"
6	"50%"

'''


def horoscope_match(sign1, sign2):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn",
        "Aquarius", "Pisces"
    ]

    idx1 = signs.index(sign1.capitalize())
    idx2 = signs.index(sign2.capitalize())

    diff = abs(idx1 - idx2)
    distance = min(diff, 12 - diff)

    compatibility_map = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    result = compatibility_map[distance]
    print(result)
    sign1 = result
    return sign1


t = horoscope_match("Libra", "Sagittarius")
print(t)
