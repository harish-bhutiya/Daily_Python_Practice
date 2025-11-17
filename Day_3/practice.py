print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Youth tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Child tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")
    add_photos = input("Do you want to take pictures? Type y for Yes and n for No. ")
    if add_photos == "y":
        #add 3$ in the bill
         bill += 3
    print(f"Your final amount is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")