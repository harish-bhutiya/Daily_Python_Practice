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

options = ["rock","paper","scissors"]

#User choice selection
your_choice = str(input("Choose your side from rock, paper or scissors.\n")).lower()
if your_choice == "rock":
    print(f"You selected : rock {rock}")
elif your_choice == "paper":
    print(f"You selected : paper {paper}")
elif your_choice == "scissors":
    print(f"You selected : scissors {scissors}")
else:
    print("Enter valid input")

 #Computer choice
computer_choice =(random.choice(options))
print(f"Computer choose : {computer_choice}")

if your_choice == "rock" and computer_choice == "paper":
    print("Computer Won!")
elif your_choice == "rock" and computer_choice == "scissors":
    print("You Won!")
elif your_choice == "rock" and computer_choice == "rock":
    print("Match Draw.")
elif your_choice == "paper" and computer_choice == "paper":
    print("Match Draw.")
elif your_choice == "paper" and computer_choice == "scissors":
    print("You Won!")
elif your_choice == "paper" and computer_choice == "rock":
    print("Computer Won!")
elif your_choice == "scissors" and computer_choice == "paper":
    print("You Won!.")
elif your_choice == "scissors" and computer_choice == "scissors":
    print("Match Draw.")
elif your_choice == "scissors" and computer_choice == "rock":
    print("Computer Won!")
else:
    print("This is out of box result.")