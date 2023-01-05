# fruits = ["apple","pear","orange"]
# for fruit in fruits:
#     print(fruit[0])
#     print(fruit + " pie


# Average Height Calculator type 1
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = total_height/number_of_students
# print(round(average_height))


# Average Height Calculator type 2
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height = total_height + height
# print(f"Total height is : {total_height}")
# number_of_students = 0
# for length in student_heights:
#     number_of_students +=1
# print(f"the total number of students are: {number_of_students}")
# average_height = round(total_height/number_of_students)
# print(f"Average height is:  {average_height}")

#Finding Mx value in a list using for loops
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# #print(student_scores)
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"The highest score in the class is :{max_score}")

#Loop with range function

# for number in range(1,11,1):
#     print(number)

#Calculate sum of all even numbers from 1 to 100
# count = 0
# for number in range(1,101,1):
#     if number % 2 == 0:
#         count = count + number
# print(count)

#FizzBuzz

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#Password generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []
#
# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)
#
# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
#
# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
#
# print(password)
# random.shuffle(password)
# print(password)
#
# final_password = ""
# for char in password:
#     final_password += char
# print(f"your final password is:  {final_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
