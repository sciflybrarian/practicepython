'''
from https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

    Write a program that asks the user how many Fibonnaci numbers to
    generate and then generates them. Take this opportunity to think
    about how you can use functions. Make sure to ask the user to enter
    the number of numbers in the sequence to generate.(Hint: The
    Fibonnaci seqence is a sequence of numbers where the next number in
    the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
print("FIBONACCI GENERATOR\n")

def getint():
    result = input("How many numbers do you want? ")
    while True:
        try:
            result = int(result)
        except ValueError:
            result = input("Please enter a whole number: ")
            continue
        if result >= 0:
            return result
        else:
            result = input("Please enter a positive number: ")

def fibgen(n):
    fib = []
    for i in range(n):
        if i < 2:
            fib.append(1)
        else:
            fib.append(fib[i-2] + fib[i-1])
    return fib
            
print(fibgen(getint()))
        
            
            