# #Subscripting
# print("Hello"[4])
# #Integers
# print(123+245)
# #Float --> Decimals
# print(126.56+12)
# #Boolean --> true or false
# print(True)

#TypeErrors
# num_char = len(input("What is your name? "))
# print(type(num_char))
# new_num_char = str(num_char)
# print(type(new_num_char))
# print("Your name has " + new_num_char + " " + "characters")
# #print("Your name has " + num_char + "characters") --> Adding string to int type gave type Error
#
# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# a=int(two_digit_number[0])
# b=int(two_digit_number[1])
# c = a+b
# print(c)

#Math operators
# print(6-2)
# print(5+2)
# print(6*2)
# print(type(6/2))
# #Exponent
# print(2**3)
#
# # For operations involving multiple operators in a single line --> PEMDAS priority
# #Parentheses,Exponents,Multiplication,Division,Addition,Subrtraction
#
# #BMI Calculator
# height =float(input("enter your height in m: "))
# weight =float(input("enter your weight in kg: "))
# bmi = weight/(height**2)
# print(type(bmi))
# print(round(bmi))

# #round() function
# print (round(8/3,2))
# print(8//3) #This will auto convert the float output to int

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
