#Subscripting

print("Hello"[0])
print("Hello"[-1])

#String
print("123" + "456")

#Interger
print(123 + 456)

#large intergers
print(123_456_789)

#float
print(3.14159)

#Boolean
print(True)
print(False)

#len function is not working in intergers

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