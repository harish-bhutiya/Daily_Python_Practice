#Subscripting

print("Hello"[0])
print("Hello"[-1])

#String
print("123" + "456")

#Interger
print(123 + 456)

#large integers
print(123_456_789)

#float
print(3.14159)

#Boolean
print(True)
print(False)

#len function is not working in integers

#Check data type by using type() function
print(type(123))
print(type(3.14159))
print(type("Hello"))
print(type(True))

#TypeCasting or change to different data type using int(), float(), str() functions
print(int("123")+int("456"))
print(float(3))
print(str("123"))
print(bool(0))
print(bool(1))

#Practice
#Question: print("Number of letter in your name: " + (len(input("Enter your name?")))

print("Number of letter in your name: " + str(len((input("Enter your name?")))))

#or

name_of_user = input("Enter your name?")
length_of_name = len(name_of_user)
print("Number of letter in your name: " + str(length_of_name))

#Mathematical Operations

print("My age is :  " + str(28))
print(5 + 3)
print(5 - 3)
print(5*3)
print(5**3)
print(5/3)
print(5//3)

#PEMDAS -Left to Right - PRIORITY
#()
#**
#* or /
#+ or -

#Example

print(3*3+3/3-3)

#Chanllege : output 3 for above equation

print(3*(3+3)/3-3)

#Assigment Operator

score = 0
#user score a point
score = score   +1

#shorthand by using assignment operator
score += 1

# Use of f-string. It is use for mix of data type

score = 1
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}, you are winning is {is_winning}")