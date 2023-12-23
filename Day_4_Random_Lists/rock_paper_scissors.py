#Rock paper scissors
import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
user_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_decision >=3 or user_decision < 0:
    print("You typed an invalid number, you lose!!")
else:
    print(game_images[user_decision])
    computer_decision = r.randint(0, 2)
    print(f"Computer chose: ")
    print(game_images[computer_decision])


    if user_decision == 0 and computer_decision ==2:
        print("You win!!")
    elif computer_decision == 0 and user_decision == 2:
        print("You lose")
    elif computer_decision > user_decision:
        print("You lose")
    elif user_decision > computer_decision:
        print("You win")
    elif computer_decision == user_decision:
        print("Its a Draw!!")
