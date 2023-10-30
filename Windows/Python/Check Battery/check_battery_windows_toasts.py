#!/usr/bin/env python3

import subprocess
from windows_toasts import WindowsToaster, Toast

battery_percent_string = "WMIC PATH Win32_Battery Get EstimatedChargeRemaining"
check_battery_percent = subprocess.check_output(battery_percent_string, shell=True)

str_battery_percent = str(check_battery_percent)

if str_battery_percent[36] == "0":
  battery_percentage = str_battery_percent[34] + str_battery_percent[35] + str_battery_percent[36]
elif str_battery_percent[35] != " ":  
  battery_percentage = str_battery_percent[34] + str_battery_percent[35]
else:
  battery_percentage = str_battery_percent[34]

toaster = WindowsToaster('Python')
newToast = Toast()
sentence_stating_current_battery = "The current battery percentage is " + battery_percentage + "%"
newToast.text_fields = [sentence_stating_current_battery]

toaster.show_toast(newToast)
