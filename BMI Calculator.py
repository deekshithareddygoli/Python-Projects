# BMI Calculator
weight = int(input("Enter the weight in kg:\n"))
height = float(input("Enter the height in m:\n"))

bmi = weight / height ** 2

print("Your Body Mass Index(BMI) Value is: ",bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("Healthy weight")
elif bmi > 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")