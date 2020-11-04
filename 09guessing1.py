'''
from https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

    Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
    guess the number, then tell them whether they guessed too low, too high, or
    exactly right. (Hint: remember to use the user input lessons from the very
    first exercise)

    Extras:
    -   Keep the game going until the user types “exit”
    -   Keep track of how many guesses the user has taken, and when the game ends,
        print this out.
'''
from random import randint

print("GUESS THE NUMBER!\n")
num = randint(1, 10)
tries = 1

while True:
    # user prompt
    if tries == 1:
        guess = input("Guess a number from 1 to 9 (or type \"exit\"): ")
    else:
        guess = input("\nTry again (or type \"exit\"): ")
        
    # quit program
    if guess.lower() == "exit":
        break
    
    # check number format
    try:
        guess = int(guess)
    except ValueError:
        print("Guess must be a whole number.")
        tries += 1
        continue
    
    # wrong answers
    if guess not in range(1, 10):
        print("Out of range!")
    elif guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
        
    # right answer
    else:
        print("That's right!")
        if tries == 1:
            print("You got it in 1 try!")
        else:
            print("You got it in " + str(tries) + " tries.")
        break
    
    tries += 1