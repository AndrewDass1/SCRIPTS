#!/usr/bin/env python3

import os

def insert_number():
	
	while True:
		try:
			brightness_level = int(input("Please enter a number from the range 0-100 to set the brightness:"))
			break
		except ValueError:
			print("Invalid input. ", end="")	
        
	if brightness_level < 0 or brightness_level > 100 or brightness_level == -0:
			print("{} is not within 0 to 100. ".format(brightness_level), end="")
			insert_number()
	else:
		adjust_brightness_command = "powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{})".format(brightness_level)

		statement = "The brightness is now {}".format(brightness_level)
		return (print(statement), os.system(adjust_brightness_command))
		
	
insert_number()
