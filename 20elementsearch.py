'''
from https://www.practicepython.org/exercise/2014/11/11/20-element-search.html:

    Write a function that takes an ordered list of numbers (a list where the
    elements are in order from smallest to largest) and another number. The
    function decides whether or not the given number is inside the list and
    returns (then prints) an appropriate boolean.

    Extras:
    - Use binary search.
'''

# Solution 1

def simplesearch(list, num):
    if num in list:
        print(True)
        return True
    else:
        print(False)
        return False

# Solution 2

def loopsearch(list, num):
    for item in list:
        if item == num:
            print(True)
            return True
        elif item > num:
            print(False)
            return False
    else:
        print(False)
        return False

# Solution 3

def binarysearch(list, num):
    newlist = list
    midpoint = int(len(newlist) / 2)
    while len(newlist) > 0:
        if newlist[midpoint] == num:
            print(True)
            return True
        elif len(newlist) == 1:
            print(False)
            return False
        elif newlist[midpoint] < num:
            newlist = newlist[midpoint + 1:len(newlist)]
        else:
            newlist = newlist[:midpoint]
        midpoint = int(len(newlist) / 2)
    else:
        print(False)
        return False

# Testing

testlists = [range(0, 15, 2), \
[], \
range(5), \
range(1, 15, 2), \
[5], \
range(6)]
'''
F
F
F
T
T
T
'''
for i in range(len(testlists)):
    simplesearch(testlists[i], 5)
    loopsearch(testlists[i], 5)
    binarysearch(testlists[i], 5)
    print()