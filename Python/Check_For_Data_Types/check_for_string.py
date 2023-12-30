#!/usr/bin/env python3

def check_for_string():
    validate_string = input("Enter a word: ")

    if validate_string.isalpha() == True:
        return print(validate_string)
    else:
        print("Not a valid word.")
        check_for_string()

check_for_string()
