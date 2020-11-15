'''
from https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

    Write a password generator in Python. Be creative with how you generate
    passwords - strong passwords have a mix of lowercase letters, uppercase
    letters, numbers, and symbols. The passwords should be random, generating a
    new password every time the user asks for a new password. Include your run-time
    code in a main method.

    Extra:
    Ask the user how strong they want their password to be. For weak passwords,
    pick a word or two from a list.
'''

# Note: skipping the main method instruction for now - will look up and revisit later

import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

words = ['Disorder', 'Wheel', 'Arrange', 'Impulse', 'Rise', 'Freight', 'Story', \
    'Deputy', 'Professor', 'Outline', 'Apology', 'Waiter', 'Trouser', 'Tactic', \
    'Cash', 'Collar', 'Negative', 'Economy', 'Excuse', 'Rhetoric', 'Eagle', \
    'Animal', 'Mole', 'Dragon', 'Golf', 'Raid', 'Pray', 'Shelter', 'Glue', \
    'Exception', 'Embox', 'Cinema', 'Dentist', 'Morale', 'Glacier', 'Degree', \
    'Dependence', 'Guarantee', 'Barrier', 'Momentum', 'Enlarge', 'Essential', \
    'Finish', 'Amber', 'Kinship', 'Conductor', 'Cry', 'Ideal', 'Inject', 'Frozen']
    # Gratitude to randomwordgenerator.com for making that part easy :)

menu = "What kind of password would you like?\n\n" + \
    "1. A secure password (randomly generated letters, numbers and symbols)\n" + \
    "2. A simple password (a randomly generated phrase)\n\n" + \
    "Your choice: "

# main program
print("PASSWORD GENERATOR\n")
while True:
    password = ""
    choice = input(menu)
    while choice != "1" and choice != "2":
        choice = input("Please enter 1 for a secure password or 2 for a simple password: ")
    # generate secure password
    if choice == "1":
        password = "".join([random.choice(characters) for x in range(12)])
    #generate simple password
    else:
        password = random.choice(words) + random.choice(words)
    print("\nYour password is: " + password)
    another = input("\nGenerate another password? (Y/N) ")
    if another.lower() != "y":
        break
    print("\n")