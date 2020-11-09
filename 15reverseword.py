'''
from https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

    Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the
    same string, except with the words in backwards order.
'''

def getstring():
    return input("Write some stuff!\n")

# Solution 1
def reverse(string):
    lst = string.split(" ")
    result = []
    for i in range(len(lst)):
        result.append(lst[len(lst)-1-i])
    return " ".join(result)

# Solution 2 (after I remembered the increment feature of list slicing) :)
def diceandslice(string):
    return " ".join(string.split(" ")[::-1])

print(diceandslice(getstring()))