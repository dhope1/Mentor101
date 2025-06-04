from reverse import reverse_string
#Importing the reverse string function in reverse.py so that i dont have to rewrite it.

def palindrome_checker(a):
    if reverse_string(a) == a:
        print("palindrome confirmed")
    else:
        print("Not A palindrome!")

#palindrome_checker("hello")
prompt1 = input("Enter a word of your choice: ")
palindrome_checker(prompt1)