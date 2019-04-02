#!/usr/bin/python
import random
x=random.randint(1,20)
for i in range(3):
	y=raw_input("Enter number between 1 and 20:")
	if int(y)==x:
		print ("correct")
	else:
		print ("Try again")
else:
	print ("Game over, correct answer is %s"%x)
