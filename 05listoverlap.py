'''
From https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

    Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    and write a program that returns a list that contains only the
    elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.

    Extras:

    1.  Randomly generate two lists to test this
    2.  Write this in one line of Python (don’t worry if you can’t
        figure this out at this point - we’ll get to it soon)
'''

# generate and print 2 random lists
from random import randint
def randlist():
    list = []
    for i in range(0, 20):
        list.append(randint(0, 100))
    return list
a = randlist()
b = randlist()
print("Lists:\n" + str(a) + "\n" + str(b) + "\n")

# compare lists, print common numbers
result = []
for num in a:
    if num in b and num not in result:
            result.append(num)
print("Numbers in common:\n" + str(sorted(result)))