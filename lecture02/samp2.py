weight = float(input("Enter ur weight in kilograms:"))
height = float(input("Enter ur height in meters:"))
bmi = weight / (height * height)

print("Your BMI is", format(bmi, '.2f'))