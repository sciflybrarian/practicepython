# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import datetime

name = input("What is your name? ")
age = input("How old are you? ")
while not age.isnumeric() or not int(age) > 0:
    age = input("Please enter a positive number: ")
else:
    age = int(age)
now = datetime.now()
turn100 = now.year - age + 100

if name == "":
    print("You will turn 100 in " + str(turn100 - 1) + " or " + str(turn100))
else:
    print(name + ", you will turn 100 in " + str(turn100 - 1) + " or " + str(turn100))