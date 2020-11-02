'''
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor of
26 because 26 / 13 has no remainder.)
'''

# initialize variables, test user input
num = input("Please enter a whole number: ")
while True:
    try:
        num = int(num)
    except ValueError:
        num = input("Please enter a whole number: ")
    else:
        break
divisors = [1]

# list and print divisors
for x in range(2, int(num/2 + 1)):
    if num % x == 0:
        divisors.append(x)
divisors.append(num)
print(divisors)