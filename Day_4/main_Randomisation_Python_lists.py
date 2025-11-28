#Randomisation and Python Lists

#Randomisation - random()
import random

#random.randint(a,b).
#Return a random integer N such that a <= N <=b.

random_integer = random.randint(1,10)
print(random_integer)

#Random Float number ramdom.random() :- 0.0 <= X <1.0

random_float_number_0_to_1 = random.random()
print(random_float_number_0_to_1)

#Random uniform :- a <= N <=b for a <= n and b <= N <=a for b < a.

random_uniform = random.uniform(1,11)
print(random_uniform)

# Head or Tails

head_tails = random.randint(0, 1)
if head_tails == 0:
    print("Head")
else:
    print("Tails")

#********** Lists **********

#Example
fruits = ["Cherry","Banana","Apple"]

#For more details visit docs.python 5th module data structure , 5.1 More on list

#Challenge

#1 option
friends = ["Alice","Bob","Charlie","David","Emanuel"]
selected_friend = random.choice(friends)
print(selected_friend)

#2nd option

random_index = random.randint(0,4)
print(friends[random_index])