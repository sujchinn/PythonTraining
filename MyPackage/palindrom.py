__author__ = 'sujchinn'

inputStr = raw_input("Enter a String to check for Palindrome: ").lower()  #case insensitivity
if (inputStr == inputStr[::-1]):
    print "The input string is palindrome"
else:
    print "The input string is not a palindrome"

