'''
http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
palindrome = False
str = input("Please enter some text: ")

for i in range(int(len(str)/2)):
	if str[i] != str[len(str) - i - 1]:
		break
else:
	palindrome = True

if palindrome:
	print("Yes, it's a palindrome!")
else:
	print("No, it's not a palindrome.")