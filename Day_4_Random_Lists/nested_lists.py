#Nested Lists
import random as r
fruits = ["apple","orange","pear","pomogrenate","Cherry"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Potatoes"]
dirty_dozen = [fruits,vegetables]
print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])
