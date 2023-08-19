#!/usr/bin/env python3
# Completed Script
import datetime, time

def timer():
    while True:
        try:
            insert_year = int(input("Enter the year number: "))
            if insert_year >= 0:
                break
        except ValueError:
            print("Not a real year number. ", end="")

    while True:
        try:
            insert_month = int(input("Enter the month number: "))
            if insert_month >= 1 and insert_month <= 12:
                break
        except ValueError:
            print("Not a real month number. ", end="")

    while True:
        try:
            insert_day = int(input("Enter the day number: "))
            if insert_month == 1 or insert_month == 3 or insert_month == 5 or insert_month == 7 or insert_month == 8 or insert_month == 10 or insert_month == 12:
                if insert_day >= 1 and insert_day <= 31:
                    break
            elif insert_month == 2:
                if insert_year % 400 == 0:
                    if insert_day >=1 and insert_day <= 29:
                        break
                elif insert_year % 4 == 0 and insert_year % 100 != 0:
                    if insert_day >=1 and insert_day <= 29:
                        break
                else:
                    if insert_day >=1 and insert_day <= 28:
                        break
            else:
                if insert_day >=1 and insert_day <= 30:
                    break
        except ValueError:
            print("Not a real month number. ", end="")

    while True:
        try:
            insert_hour = int(input("Enter the hour number: "))
            if insert_hour >= 0 and insert_hour <= 23:
                break
        except ValueError:
            print("Not a real hour number. ", end="")

    while True:
        try:
            insert_minute = int(input("Enter the minute number: "))
            if insert_minute >= 0 and insert_minute <= 59:
                break
        except ValueError:
            print("Not a real minute number. ", end="")

    while True:
        try:
            insert_seconds = int(input("Enter the amount of seconds: "))
            if insert_seconds >= 0 and insert_seconds <= 59:
                break
        except ValueError:
            print("Not a real second number. ", end="")

    inserted_time = datetime.datetime(insert_year, insert_month, insert_day, insert_hour, insert_minute, insert_seconds)
    print("The timer will stop when it reaches this date and time:", inserted_time)

    while True:
        if datetime.datetime.now() > inserted_time:
            break
        else:
            print("Current time:", datetime.datetime.now())
            print("Time is still going...")
            difference_in_time = inserted_time - datetime.datetime.now()
            print("Time left: ", difference_in_time)

            if (difference_in_time.total_seconds()) > 10:
                time.sleep(10)
                print("10 seconds has passed.")
            else:
                time.sleep(difference_in_time.total_seconds())
                print("Less than 10 seconds has passed.")

    print("Program Finished.")

timer()
