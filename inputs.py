# Here we are prompting the user for their name and age, and storing them in variables
print("What is your name?")
name=input()

print("How old are you?")
age=int(input())

print(name)
print(age)

# Using the **sys** Module
import sys

# Here we have first imported the sys module so that we could use sys.argv to store user input from the console and store it in a list
import sys
name=sys.argv[1]

print("Enter your age")
age=int(input())
