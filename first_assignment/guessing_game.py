#!/usr/bin/python
import random
answer=random.randint(1,20)
name=raw_input("Please enter your name:")
print ("Hi %s, I want us to play a little guessing game."%name)
print ("I am going to give you three chances to guess a number between 1 and 20")
i=0

while i<3:
    guess=raw_input("Please enter a number between 1 and 20:")
    i+=1
    if int (guess)==answer:
        print ("Congratulations, %s is the correct answer"%guess)
        print ("You had %d tries"%i)
        break
    elif i<3:
        print ("That's Wrong. Try again")
    elif i==3:
        print ("Tough Luck %s!!"%name)
	print ("You've exhausted all 3 tries, the correct answer is %d"%answer)
print("Goodbye")
