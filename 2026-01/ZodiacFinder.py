'''
Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:

Date Range	Zodiac Sign
March 21 - April 19	"Aries"
April 20 - May 20	"Taurus"
May 21 - June 20	"Gemini"
June 21 - July 22	"Cancer"
July 23 - August 22	"Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	"Pisces"
Zodiac signs are based only on the month and day, you can ignore the year.
'''


def get_sign(date_str):
    result = None
    year, month, day = date_str.split("-")

    if month == "01":
        if int(day) <= 19:
            return "Capricorn"
        else:
            return "Aquarius"
    elif month == "02":
        if int(day) <= 18:
            return "Aquarius"
        else:
            return "Pisces"
    elif month == "03":
        if int(day) <= 20:
            return "Pisces"
        else:
            return "Aries"
    elif month == "04":
        if int(day) <= 19:
            return "Aries"
        else:
            return "Taurus"
    elif month == "05":
        if int(day) <= 20:
            return "Taurus"
        else:
            return "Gemini"
    elif month =="06":
        if int(day) <= 20:
            return "Gemini"
        else:
            return "Cancer"
    elif month == "07":
        if int(day) <= 22:
            return "Cancer"
        else:
            return "Leo"
    elif month == "08":
        if int(day) <= 22:
           return "Leo"
        else:
            return "Virgo"
    elif month == "09":
        if int(day) <= 22:
            return "Virgo"
        else:
            return "Libra"
    elif month == "10":
        if int(day) <= 22:
            return "Libra"
        else:
            return "Scorpio"
    elif month == "11":
        if int(day) <= 21:
            return "Scorpio"
        else:
            return "Sagittarius"
    elif month == "12":
        if int(day) <= 18:
            return "Sagittarius"
        else:
            return "Capricorn"


    return date_str


t = get_sign("2026-01-31")
print(t)
