'''
from https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
    plays (using input), compare them, print out a message of congratulations
    to the winner, and ask if the players want to start a new game)

    Remember the rules:

    -   Rock beats scissors
    -   Scissors beats paper
    -   Paper beats rock
'''

import random
playing = True

'''
dict setup: each item is paired with the item it beats in the game,
i.e. "rock": "scissors" means "rock beats scissors"
'''
choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

print("ROCK PAPER SCISSORS!\n")

while playing:
    # get and check player choice
    print("One, two, three, SHOOT!")
    playerchoice = input("Your choice: ")
    while playerchoice.lower() not in choices:
        playerchoice = input("Please enter rock, paper, or scissors: ")
    playerchoice = playerchoice.lower()
    
    # computer chooses at random
    compchoice = random.choice(list(choices))
    print("The computer chose " + compchoice + ".")
    
    # determine winner
    if playerchoice == choices[compchoice]:
        print("Computer wins!")
    elif compchoice == choices[playerchoice]:
        print("Player wins!")
    else:
        print("It's a tie!")
        
    # ask to replay
    playagain = input("\nPlay again? (Y/N) ")
    if playagain.lower() != "y":
        playing = False
