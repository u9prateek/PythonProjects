rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
gamelist = [rock,paper,scissors]
usrchoice = gamelist[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]
print(usrchoice)
compchoice = gamelist[random.randint(0,2)]
print("Computer chose")
print(compchoice)
if usrchoice == compchoice:
    print("Tie")
else:
    if (usrchoice==rock or usrchoice==paper) and (compchoice==rock or compchoice==paper):
        if usrchoice == paper:
            print("You won")
        else:
            print("You lose")
    if (usrchoice==rock or usrchoice==scissors) and (compchoice==rock or compchoice==scissors):
        if usrchoice == rock:
            print("You won")
        else:
            print("You lose")
    if (usrchoice==paper or usrchoice==scissors) and (compchoice==paper or compchoice==scissors):
        if usrchoice == scissors:
            print("You won")
        else:
            print("You lose")
