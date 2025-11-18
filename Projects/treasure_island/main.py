print(r"""
__________
        /\____;;___/\
       | /         |/
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       %%%%
""")

print('''
Welcome to the Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?
''')

left_right = str(input('''     Type "left" or "right"\n''')).lower()

if left_right == "left":
    print("Swim or Wait")
    swim_wait = str(input("You've  come to a lake. "
                          "there is an island in the middle of the lake."
                          "type 'wait' to wait for a boat."
                          " Type 'swim' to swim across \n")).lower()
    if swim_wait == "wait":
        print("Which door?")
        door_colour = str(input("You arrived at island unharmed."
                                "There is house with 3 doors."
                                "one red, one yellow and one blue. "
                                "Which colour do you choose?\n")).lower()
        if door_colour == "yellow":
            print("You found the treasure."
                  "You Win!")
        elif door_colour == "red":
            print("It's a room full of fire."
                  "Game Over")
        elif door_colour == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Please enter valid input.")
    else:
        print("You got attacked by an angry trout.")
else:
    print("Game over")
