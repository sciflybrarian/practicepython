'''
from https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
    
    This week’s exercise is going to be revisiting an old exercise
    (see Exercise 5), except require the solution in a different way.

    Take two lists, say for example these two:

        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    and write a program that returns a list that contains only the
    elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
    Write this using at least one list comprehension.
    
    Extra: Randomly generate two lists to test this
'''

from random import randint
def randlist():
    return [randint(1, 100) for i in range(0, randint(10, 20))]

a = randlist()
b = randlist()
result = [a[i] for i in range(len(a)) if a[i] in b and a[i] not in a[:i]]