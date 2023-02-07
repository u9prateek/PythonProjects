# This code meant to run Reborgs's world website in "Maze" world
# URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Creating turn right function using turn left function
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Variable "r" is used to make sure reborg is not stuck in turn right loop in certain cases
r = 0
while at_goal() == False:
# r less than 4 make sure reborg cannot make more than 3 times continously and thus avoiding a loop
    if right_is_clear() and r < 4:
        r +=1
        turn_right()
        move()
    elif front_is_clear():
        r = 0
        move()
    else:
        r = 0
        turn_left()