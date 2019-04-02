#!/usr/bin/python
age=int(raw_input("Enter your age:"))
if age<=12 and  age > 0:
    print ("Kid")
elif age>12 and age <=19 :
    print("Teen")
elif age>19 and age <=35:
    print("Young adult")
elif age>35 and age<=60:
    print("Adult")
else:
    print ("Senior Citizen")
