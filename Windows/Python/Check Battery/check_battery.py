#!/usr/bin/env python3

import subprocess
from win10toast import ToastNotifier

battery_percent_string = "WMIC PATH Win32_Battery Get EstimatedChargeRemaining"
check_battery_percent = subprocess.check_output(battery_percent_string, shell=True)

str_battery_percent = str(check_battery_percent)

if str_battery_percent[36] == "0":
  battery_percentage = str_battery_percent[34] + str_battery_percent[35] + str_battery_percent[36]
elif str_battery_percent[35] != " ":  
  battery_percentage = str_battery_percent[34] + str_battery_percent[35]
else:
  battery_percentage = str_battery_percent[34]

int_battery_percentage = int(battery_percentage)

display_message = ToastNotifier()

if int_battery_percentage == 100:
  display_message.show_toast("BATTERY LEVEL", "Battery is at {}%".format(battery_percentage), duration=10)
else:
  display_message.show_toast("BATTERY LEVEL", "Battery is at {}%".format(battery_percentage), duration=10)
