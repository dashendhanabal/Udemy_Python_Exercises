# print("Welcome to the rollercoaster ride!!")
# height = int(input("What is your height? ")) # This is assignment
# if height == 120: # This is checking equality
#     print("Here is your ticket!!!")
# else:
#     print("You are too short")

# Odd Even Number
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

#Nested if Else
# print("Welcome to the rollercoaster ride!!")
# height = int(input("What is your height? ")) # This is assignment
# if height >= 120: # This is checking equality
#     # print("Here is your ticket!!!")
#     age = int (input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5")
#
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("You are too short")

#BMI 2.0

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = int(weight/(height**2))
# if bmi <= 18.5:
#     print(f"Your bmi is {bmi}, You are underweight")
# elif 18 < bmi <=25:
#     print(f"Your bmi is {bmi},You are at a normal weight")
# elif 25< bmi <=30:
#     print(f"Your bmi is {bmi},You are slightly overweight")
# elif 30< bmi <=35:
#     print(f"Your bmi is {bmi},You are obese")
# else:
#     print(f"Your bmi is {bmi},You are clinically obese")

#Leap year

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 ==0:
#         if year % 400 ==0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
#
# else:
#      print("Not Leap Year")

#Multiple If Conditions
# print("Welcome to the rollercoaster ride!!")
# height = int(input("What is your height?(in cm) ")) # This is assignment
# if height >= 120: # This is checking equality
#     age = int (input("What is your age? "))
#     if age <= 12:
#         bill= 5
#         photo = str(input("Do you want your photo taken? "))
#         if photo == "yes":
#             total_bill = bill +3
#             print(f"Please pay ${total_bill}")
#         else:
#             print(f"Please pay ${bill}")
#     elif age <= 18:
#         bill= 7
#         photo = str(input("Do you want your photo taken? "))
#         if photo == "yes":
#             total_bill = bill +3
#             print(f"Please pay ${total_bill}")
#         else:
#             print(f"Please pay ${bill}")
#     elif age > 18:
#         bill= 12
#         photo = str(input("Do you want your photo taken? "))
#         if photo == "yes":
#             total_bill = bill +3
#             print(f"Please pay ${total_bill}")
#         else:
#             print(f"Please pay ${bill}")
#
# else:
#     print("You are too short")

#Python Pizza

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese =="Y":
#         bill +=1
#     print(f"Your final bill is: ${bill}")
# elif size=="M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill +=3
#     if extra_cheese =="Y":
#         bill +=1
#     print(f"Your final bill is: ${bill}")
#
# elif size=="L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese =="Y":
#         bill +=1
#     print(f"Your final bill is: ${bill}")

#Love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# actual_name_1 = name1.lower()
# actual_name_2 = name2.lower()
# true_score = actual_name_1.count("t") + actual_name_1.count("r") + actual_name_1.count("u") + actual_name_1.count("e") + actual_name_2.count("t") + actual_name_2.count("r") + actual_name_2.count("u") + actual_name_2.count("e")
# love_score = actual_name_1.count("l") + actual_name_1.count("o") + actual_name_1.count("v") + actual_name_1.count("e") + actual_name_2.count("l") + actual_name_2.count("o") + actual_name_2.count("v") + actual_name_2.count("e")
# total_score = str(true_score) + str(love_score)
# total_score_value = int(total_score)
# if total_score_value < 10 or total_score_value >90:
#     print(f"Your score is {total_score_value}, you go together like coke and mentos.")
# elif 40<total_score_value<50:
#         print(f"Your score is {total_score_value}, you are alright together.")
# else:
#     print(f"Your score is {total_score_value}")

# Treasure Island Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You're at a crossroad, Where do you choose to go? Type left or right\n").lower()
if choice_1 =="left":
    choice_2 = input("You have come to a lake, Type wait to wait for a boat or type swim to swim across the lake\n").lower()
    if choice_2 == "wait":
        choice_3 = input("You have reached the island unharmed, Which door will you pick? Red Yellow or Blue? \n").lower()
        if choice_3 == "red" or choice_3 == "blue":
            print("No treasure Found, GAME OVER!")
        elif choice_3 == "yellow":
            print("YOU WON THE TREASURE")
        else:
            print("Invalid Input")
    else:
        print("You have been eaten by SHARKS!!!")
else:
    print("Wrong direction, you are lost forever!")
