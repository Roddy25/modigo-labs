def bmi_report(weight_kg, height_m):
    # TODO: calculate bmi, round it to 1 decimal place, determine the category,
    # and return "BMI: {bmi}, Category: {category}"
    bmi = round(weight_kg / (height_m ** 2), 1)
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        category = "Normal weight"
    elif bmi >= 25.0 and bmi <= 29.9:
        category = "Overweight"
    elif bmi >= 30.0:
        category = "Obese"
    return f"BMI: {bmi}, Category: {category}"
print(bmi_report(50, 1.70))