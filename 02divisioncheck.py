# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# extra credit: have user choose a divisor

# To check number format
def floaty(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

playing = True
keepplaying = ""

print("Welcome to the Division Checker!")

while playing:
    print()

    # get user input, check format
    num = input("Please enter a number: ")
    while not floaty(num):
        num = input("Please enter a number: ")

    div = input("Please choose a number to divide by: ")
    while not floaty(div):
        div = input("Please choose a number to divide by: ")
    print()

    # determine and print result
    if float(num) % float(div) == 0:
        print(num + " is divisible by " + div + "!")
    else:
        print(num + " is not divisible by " + div + ".")
    print()

    # ask to replay program
    keepplaying = input("Check another number? (y/n) ")
    if keepplaying[0].lower() != "y":
        playing = False

print()
print("Thanks for using the Division Checker!")