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