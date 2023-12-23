#BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = int(weight/(height**2))
if bmi <= 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif 18 < bmi <=25:
    print(f"Your bmi is {bmi},You are at a normal weight")
elif 25< bmi <=30:
    print(f"Your bmi is {bmi},You are slightly overweight")
elif 30< bmi <=35:
    print(f"Your bmi is {bmi},You are obese")
else:
    print(f"Your bmi is {bmi},You are clinically obese")
