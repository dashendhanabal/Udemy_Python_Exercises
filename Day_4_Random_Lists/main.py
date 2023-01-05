import random as r

# random_integer = r.randint(1,10)
# random_float = r.random()
# random_float_rounded = round(random_float, 2)
# print(random_integer)
# print(random_float)
# print(random_float_rounded)

# Random Heads/Tails
# random_side=r.randint(0,1)
# if random_side == 1:
#     print(random_side)
#     print("Heads")
# else:
#     print(random_side)
#     print("Tails")

#Lists

# fruits = ["apple","orange","pear","pomogrenate","Cherry"]
# print(fruits)
# print(fruits[0])
# print(fruits[-2])
#
# fruits[2] = "Blueberry"
# print(fruits)
# print(fruits[2])

#Bankers Roulette
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# #print(names)
# random_value = r.randint(0,len(names)-1)
# print(random_value)
# print(f"{names[random_value]} is going to buy the meal today!")

#Nested Lists
# fruits = ["apple","orange","pear","pomogrenate","Cherry"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Potatoes"]
# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1])

#Treasure map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")

#Rock paper scissors

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock,paper,scissors]
# user_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_decision >=3 or user_decision < 0:
#     print("You typed an invalid number, you lose!!")
# else:
#     print(game_images[user_decision])
#     computer_decision = r.randint(0, 2)
#     print(f"Computer chose: ")
#     print(game_images[computer_decision])
#
#
#     if user_decision == 0 and computer_decision ==2:
#         print("You win!!")
#     elif computer_decision == 0 and user_decision == 2:
#         print("You lose")
#     elif computer_decision > user_decision:
#         print("You lose")
#     elif user_decision > computer_decision:
#         print("You win")
#     elif computer_decision == user_decision:
#         print("Its a Draw!!")
