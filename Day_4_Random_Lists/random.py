import random as r

random_integer = r.randint(1,10)
random_float = r.random()
random_float_rounded = round(random_float, 2)
print(random_integer)
print(random_float)
print(random_float_rounded)

#Random Heads/Tails
random_side=r.randint(0,1)
if random_side == 1:
    print(random_side)
    print("Heads")
else:
    print(random_side)
    print("Tails")

#Lists

fruits = ["apple","orange","pear","pomogrenate","Cherry"]
print(fruits)
print(fruits[0])
print(fruits[-2])

fruits[2] = "Blueberry"
print(fruits)
print(fruits[2])
