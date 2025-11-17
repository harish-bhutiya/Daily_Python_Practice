#Control flow with if/ else and Conditional Operators

#if / else condition

# if condition:
  #do this
# else:
  #do this

# Let check example of

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

#Comparison Operators

# > Greater than
# < less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to (When to equal is for checking value is same on left and right)
# != Not equal to

#New operator

# Modulo Operator %(Reminder)

# 10 % 5 answer is 0. Here it shows that 5 goes to 2 times in 10 and no reminder left
# 10 % 3 answer is 1. Here 3 goes 3 times in 10 and 1 reminder left

# Let take challenge

print("Let find out the given input is Even or ODD")

number_1 = int(input("Write a number "))
number_2 = int(input("Write a number "))
final_output = int(number_1%number_2)

if final_output % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# Nested if / else

#if condition:
    #if another condition:
      #do this
    #else:
      #do this
#else:
  #do this

# Example

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your height in cm? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# if / elif / else

print("Welcome to the Drink shop.")
age = int(input("How old are you? \n"))

if age >18:
    print("You are allowed to buy any drinks")
elif age >=12:
    print("You allowed to buy soft drinks")
elif age >= 16:
    print("You are allowed to buy energy drink")
else:
    print("Children are not allowed in this shop")

# Pizza order app

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

# Multiple condition (Logical operators)

# Roller coaster ride with logical operator
print("Welcome to the rollercoaster ride")
check_height = int(input("Please enter your height in cm."))
bill = 0

if check_height > 120:
    print("You are allowed to enter to the park.")
else:
    print("You are require to at least 120cm to enter in to park")
#Price for different age range.

check_age = int(input("Please enter your age.\n"))

if check_age <= 12 :
    bill = 5
    print(f"You have to pay ${bill}")
elif check_age <= 18:
    bill = 7
    print(f"You have to pay ${bill}")

elif 45 <= check_age <= 55:
    print("Your visit is free for today")

elif check_age > 18:
    bill = 12
    print(f"You have to pay ${bill}")

else:
    print("Please enter valid input.")




