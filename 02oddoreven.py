# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Number checker
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

playing = True
keepplaying = ""

print("Welcome to the Number Checker!")

while playing:
    print()
    # get user input, check format
    num = input("Please enter a number: ")
    while not is_float(num):
        num = input("Please enter a number: ")

    # Determine and print result
    if float(num) % 1 != 0:
        print("Your number is a decimal!")
    elif float(num) % 2 == 0:
        if float(num) % 4 == 0:
            print("Your number is even and divisible by 4!")
        else:
            print("Your number is even!")
    else:
        print("Your number is odd!")
    print()

    keepplaying = input("Check another number? (y/n) ")
    if keepplaying[0].lower() != "y":
        playing = False
        print()
        print("Thanks for using the Number Checker!")