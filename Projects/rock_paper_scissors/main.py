#rock paper scissors game
import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = ('''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')

options = ["rock", "paper", "scissors"]
ascii_dict = {"rock": rock, "paper": paper, "scissors": scissors}

# User choice selection
your_choice = input("Choose your side from rock, paper or scissors.\n").lower()

if your_choice not in options:
    print("Enter valid input")
    exit()

# Computer choice
computer_choice = random.choice(options)

print(f"You selected : {your_choice} {ascii_dict[your_choice]}")
print(f"Computer selected : {computer_choice} {ascii_dict[computer_choice]}")

# Game Logic
if your_choice == computer_choice:
    print("Match Draw.")
elif (your_choice == "rock" and computer_choice == "scissors") or \
     (your_choice == "scissors" and computer_choice == "paper") or \
     (your_choice == "paper" and computer_choice == "rock"):
    print("You Won!")
else:
    print("Computer Won!")
