#Bankers Roulette
import random as r
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#print(names)
random_value = r.randint(0,len(names)-1)
print(random_value)
print(f"{names[random_value]} is going to buy the meal today!")
