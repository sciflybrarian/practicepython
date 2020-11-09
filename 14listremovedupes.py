'''
from https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

    Write a program (function!) that takes a list and returns a new list that contains
    all the elements of the first list minus all the duplicates.

Extras:

    -   Write two different functions to do this - one using a loop and constructing a
        list, and another using sets.
    -   Go back and do Exercise 5 using sets, and write the solution for that in a
        different function.
'''

def dedupeloop(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] not in lst[:i]:
            result.append(lst[i])
    return result

def dedupeset(lst):
    return list(set(lst))

'''
Exercise 5 redux: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

    Take two lists [...] and write a program that returns a list that contains only the
    elements that are common between the lists (without duplicates).
'''

def listoverlap(lst1, lst2):
    result = set()
    for item in lst1:
        if item in lst2:
            result.add(item)
    return list(result)