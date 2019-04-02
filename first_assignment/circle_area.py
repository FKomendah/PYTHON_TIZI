#!/usr/bin/python
pi=3.142

def circle_area(radius):
    area=pi*radius*radius
    return area


b=raw_input("Enter the radius:")
a=circle_area(float(b))
print (a)
