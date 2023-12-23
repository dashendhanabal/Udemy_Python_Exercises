#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
actual_name_1 = name1.lower()
actual_name_2 = name2.lower()
true_score = actual_name_1.count("t") + actual_name_1.count("r") + actual_name_1.count("u") + actual_name_1.count("e") + actual_name_2.count("t") + actual_name_2.count("r") + actual_name_2.count("u") + actual_name_2.count("e")
love_score = actual_name_1.count("l") + actual_name_1.count("o") + actual_name_1.count("v") + actual_name_1.count("e") + actual_name_2.count("l") + actual_name_2.count("o") + actual_name_2.count("v") + actual_name_2.count("e")
total_score = str(true_score) + str(love_score)
total_score_value = int(total_score)
if total_score_value < 10 or total_score_value >90:
    print(f"Your score is {total_score_value}, you go together like coke and mentos.")
elif 40<total_score_value<50:
        print(f"Your score is {total_score_value}, you are alright together.")
else:
    print(f"Your score is {total_score_value}")
