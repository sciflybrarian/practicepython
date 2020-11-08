'''
from https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

    Ask the user for a number and determine whether the number is prime or not.
    (For those who have forgotten, a prime number is a number that has no
    divisors.). You can (and should!) use your answer to Exercise 4 to help
    you. Take this opportunity to practice using functions, described below.
'''

def getint():
    result = ""
    while True:
        result = input("Please enter a whole number: ")
        try:
            result = int(result)
        except ValueError:
            continue
        else:
            return result

def isprime(num):
    if num < 2:
        return False
    for x in range(2, int(num/2) + 1):
        if num % x == 0:
            return False
    else:
        return True
    
print(isprime(getint()))