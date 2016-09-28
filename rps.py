'''This is a simple program to play rock, paper, scissors against the computer.'''

from random import randint
from time import sleep

options = ["R", "P", "S"]
WIN_MSG = "Congratulations! You beat the computer."
LOSE_MSG = "The computer wins! You lose!"

def decide_winner(user_choice, computer_choice):
    print("You selected: %s" % user_choice)
    #TODO: Ensure that whole word prints instead of just first letter
    print("Computer selecting...")
    sleep(1)
    print("The computer has chosen %s" % computer_choice)
    #TODO: Validate for answers not within the options array
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)


#winning scenarios
    if user_choice_index == computer_choice_index:
        print("Tie!")
    elif user_choice_index == 0 and computer_choice_index == 2:
        print(WIN_MSG)
    elif user_choice_index == 1 and computer_choice_index == 0:
        print(WIN_MSG)
    elif user_choice_index == 2 and computer_choice_index == 0:
        print(WIN_MSG)
    elif user_choice_index > 2:
        print("Your answer is garbage and you should feel like garbage.")
        return
    else:
        print(LOSE_MSG)

#actual gameplay
def play_RPS():
    print("Time to play Rock, Paper, Scissors. As you know, Rock beats Scissors, Paper beats Rock, and Scissors beats Paper.")
    user_input = raw_input("Take your pick- Rock, Paper, or Scissors? ")
    user_choice = user_input[:1].upper()
    #TODO: Validate for answers that start with R, P, or S but which are not in the array
    sleep(1)
    computer_choice = options[randint(0, (len(options) - 1))]

    decide_winner(user_choice, computer_choice)
play_RPS()
