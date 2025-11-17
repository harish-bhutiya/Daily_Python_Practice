print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want to add extra cheese? Y or N:\n")
total_bill = 0

if size == "S":
    total_bill = 15
    if add_pepperoni == "Y":
     total_bill += 2


    if extra_cheese == "Y":
     total_bill += 1
    print(f"Your small size pizza is for {total_bill}$")

elif size == "M":
    total_bill = 20

    if add_pepperoni == "Y":
     total_bill += 3


    if extra_cheese == "Y":
     total_bill += 1
    print(f"Your Medium size pizza is for {total_bill}$")

elif size == "L":
    total_bill = 25

    if add_pepperoni == "Y":
     total_bill += 3

    if extra_cheese == "Y":
     total_bill += 1
    print(f"Your Large size pizza is for {total_bill}$")
else:
    print("Please select your pizza size.")


# Other way to do above code

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want to add extra cheese? Y or N:\n")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input")

# todo: work out how much to add to their bill based on their pepperoni choice.
if add_pepperoni == "Y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")