#Nested if Else
print("Welcome to the rollercoaster ride!!")
height = int(input("What is your height? ")) # This is assignment
if height >= 120: # This is checking equality
    # print("Here is your ticket!!!")
    age = int (input("What is your age? "))
    if age <= 12:
        print("Please pay $5")

    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You are too short")
