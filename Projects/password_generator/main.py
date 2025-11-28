#Password Generator
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*",
           "(", ")", "-", "_", "+", "=", "{", "}", "[", "]",
           "|", r"\\", ":", ";", r"\"", "'", "<", ",", ">", ".",
           "?", "/"]

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
random_letter_choices = random.choices(letters, k=nr_letters)
# print("".join(random_letter_choices))

nr_numbers = int(input("How many numbers would you like?\n"))
random_number_choices = random.choices(numbers, k = nr_numbers)
# print("".join(random_number_choices))

nr_symbols = int(input("How many symbols would you like?\n"))
random_symbol_choices = random.choices(symbols, k = nr_symbols)
# print("".join(random_symbol_choices))

password_output = random_letter_choices+random_number_choices+random_symbol_choices
print("".join(password_output))

#mixed password

random.shuffle(password_output)
print("".join(password_output))
