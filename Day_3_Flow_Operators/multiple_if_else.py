#Multiple If Conditions
print("Welcome to the rollercoaster ride!!")
height = int(input("What is your height?(in cm) ")) # This is assignment
if height >= 120: # This is checking equality
    age = int (input("What is your age? "))
    if age <= 12:
        bill= 5
        photo = str(input("Do you want your photo taken? "))
        if photo == "yes":
            total_bill = bill +3
            print(f"Please pay ${total_bill}")
        else:
            print(f"Please pay ${bill}")
    elif age <= 18:
        bill= 7
        photo = str(input("Do you want your photo taken? "))
        if photo == "yes":
            total_bill = bill +3
            print(f"Please pay ${total_bill}")
        else:
            print(f"Please pay ${bill}")
    elif age > 18:
        bill= 12
        photo = str(input("Do you want your photo taken? "))
        if photo == "yes":
            total_bill = bill +3
            print(f"Please pay ${total_bill}")
        else:
            print(f"Please pay ${bill}")

else:
    print("You are too short")
