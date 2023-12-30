#!/usr/bin/env python3

def declare_variable():

    while True:
	    try:
		    pass_a_number = int(input("Please enter a number: "))
		    break
	    except ValueError:
		    print("Invalid input. ", end="")

    if pass_a_number != int(pass_a_number):
        print(declare_variable())
    else:
        return "The integer " + str(pass_a_number) + " was passed."
	
print(declare_variable())
