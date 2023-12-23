#Calculate sum of all even numbers from 1 to 100
count = 0
for number in range(1,101,1):
    if number % 2 == 0:
        count = count + number
print(count)
