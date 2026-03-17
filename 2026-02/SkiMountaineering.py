'''
2026 Winter Games Day 14: Ski Mountaineering
Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

"Shallow"	"Moderate"	"Deep"
"Gentle"	"Safe"	"Safe"	"Safe"
"Steep"	"Safe"	"Risky"	"Risky"
"Very Steep"	"Safe"	"Risky"	"Risky"
'''


def avalanche_risk(snow_depth, slope):
    if snow_depth == "Shallow":
        return "Safe"
    if slope == "Gentle":
        return "Safe"
    result = "Risky"
    snow_depth = result

    return snow_depth


t = avalanche_risk("Shallow", "Gentle")
print(t)
