# F-string --> Use this if you want to add diff data types into a string output
score=32
height=1.8
isWinning=True
print(f"ths score is {score}, height is {height}, Man Utd winning is {isWinning}")

# Life in Weeks
age = input("What is your current age? ")
years_left = 90 - int(age)
num_years_left = int(years_left)
days_left = num_years_left * 365
weeks_left = num_years_left * 52
months_left = num_years_left * 12
print(f"you have {days_left} days, {weeks_left} weeks and {months_left} months left")

#Tip Calculator
print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage_of_tip = float(input("What percentage of tip would you like to give? 10, 12 or 15?"))
num_of_people = int(input("How many people to split the bill?"))
final_bill = round((total_bill/num_of_people)*(percentage_of_tip+100)/100,2)
print(f"Each person should pay ${final_bill}")
