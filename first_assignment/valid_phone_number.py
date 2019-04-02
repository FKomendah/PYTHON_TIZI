#!/usr/bin/python
def valid_phone_number(number):
        if len(number)==10 and number.startswith("07"):
                print ("That is a valid phone nunber")
        else:
                print ("That is not a valid phone number")

my_number=raw_input("Enter your phone number:")
valid_phone_number(my_number)

