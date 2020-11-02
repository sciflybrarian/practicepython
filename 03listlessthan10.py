'''
From https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

    Take a list [...] and write a program that prints out all the elements of the list that are less than 5.

    Extras:
    1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    2. Write this in one line of Python.
    3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

# example list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Solution 1
for num in a:
    if num < 5:
        print(num)
        
# Solution 2 (Extras 1 and 2)
print([num for num in a if num < 5])

# Solution 3 (Extra 3)
bound = int(input("Please enter a number: "))
print([num for num in a if num < bound])