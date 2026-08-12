'''
BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.

To get BMI: divide the weight by the height squared, then multiply the result by 703.

'''

def calculate_bmi(weight, height):
    bmi_total = (weight / pow(height,2)) * 703
    # print(bmi_total)
    result = f"{bmi_total:.1f}"
    print(result)

    weight = float(result)
    print(type(weight))
    return weight

t = calculate_bmi(180, 70)
print(t)