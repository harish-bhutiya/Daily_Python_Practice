#Loops

#For Loop

# fruits = ["Apple","Peach","Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "  pie")
#     print(fruits)

student_scores = [180,124,165,173,189,169,146]
print(max(student_scores)) #Will print higher number in list

#range function with for loop

for number in range(1,11):  #it will print 1 to 10
    print(number)

#if you want increment with intervals of 3

for number in range(1,11,3):
    print(number)

total_number = 0

#The Gauss challenge

for number in range(1,101):
    total_number += number
print(total_number)
