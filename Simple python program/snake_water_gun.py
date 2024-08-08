# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
# where players use hand gestures to represent a snake, water, or a gun.
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.

import random


def check(computer, user):
    if computer == user:
        return 0

    if computer == 0 and user == 1:
        return -1

    if computer == 1 and user == 2:
        return -1

    if computer == 2 and user == 0:
        return -1

    return 1


user = int(input("0 for snake ,1 for  water ,2 for gun :\n"))
computer = random.randint(0, 2)

score = check(computer, user)

print("You:", user)
print("Computer:", computer)

if score == 0:
    print("It's a tie!")

elif score == -1:
    print("You lose!")

else:
    print("You win!")
