print("""         __________________
       .-'  \ _.-''-._ /  '-.
     .-/\   .'.      .'.   /\-.
    _'/  \.'   '.  .'   './  \'_
   :======:======::======:======:  
    '. '.  \     ''     /  .' .'
      '. .  \   :  :   /  . .'
        '.'  \  '  '  /  '.'
          ':  \:    :/  :'
            '. \    / .'
              '.\  /.'
                '\/'""")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("""You\'re at a cross road. Where do you want to go? Type "left" or "right" \n""")
if road.lower() == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')
    if lake.lower() == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        if house.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif house.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        elif house.lower() == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")