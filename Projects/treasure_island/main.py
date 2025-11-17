print('''
__________
        /\____;;___\_
       | /         /
       `. ())oo() .
        |\(%()*^^()^\_
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       %%%%
''')

print('''
Welcome to the Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?
''')

left_right = str(input('''     Type "left" or "right"\n''')).lower()

if left_right == "left":
    print("Swim or Wait")
    left_right = str(input('''     Type "left" or "right"\n''')).lower()
    if left_right == "left":
        print("Which door?")
        door_colour = str(input("Red,Yellow,Blue")).lower()
        if door_colour == "yellow":
            print("You Win!")
        elif door_colour == "red":
            print('''
            Burned by Fire.
            Game Over.
            ''')
        elif door_colour == "blue":
            print('''
            Eaten by beasts.
            Game Over.
            ''')
        else:
            print("Please enter valid input.")
else:
    print("Game over")
