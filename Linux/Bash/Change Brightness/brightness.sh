#!/bin/bash

read -p "Choose '1' to enter a brightness number or choose '2' a percentage: " brightness_choice
echo "Option chosen: "$brightness_choice

if [ $brightness_choice -eq 1 ] 
then
        read -p "Enter a number from 0 (minimum brightness) to 19200 (maximum brightness): " brightness_number
        sudo brightnessctl -d "intel_backlight" set $brightness_number
elif [ $brightness_choice -eq 2 ] 
then
        read -p "Enter a number for the brightness percentage: " brightness_percentage
        sudo brightnessctl -d "intel_backlight" set $brightness_percentage%
else
        echo "Not a valid option. Try again."
fi
