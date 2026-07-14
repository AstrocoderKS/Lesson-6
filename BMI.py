H = float(input("What is your height in metres?"))
W = float(input("What is your weight in kilograms?"))

BMI = W / H**2
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <=29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are severly overweight.")
else:
    print("You are severely obese.")