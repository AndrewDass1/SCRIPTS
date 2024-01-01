#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

zip_code = int(input("Enter Zip Code:"))
str_zip_code = str(zip_code)

if len(str_zip_code) <= 4:
    while len(str_zip_code) <= 4:
        str_zip_code = '0' + str_zip_code
    url = 'https://weather.com/weather/today/l/' + str_zip_code
elif len(str_zip_code) == 5:
    url = 'https://weather.com/weather/today/l/' + str_zip_code
else:
    print("Enter a five digit zip code next time.")
    quit()

using_requests = requests.get(url)
soup = BeautifulSoup(using_requests.content, 'html.parser')

html_div = soup.find(id="WxuAirQuality-sidebar-aa4a4fb6-4a9b-43be-9004-b14790f57d73")

str_html_div = str(html_div)
list_of_string_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

if str_html_div[1329] in list_of_string_num:  
    air_quality = str_html_div[1327] + str_html_div[1328] + str_html_div[1329]
    print("The air quality is:", air_quality)
else:
    air_quality = str_html_div[1327] + str_html_div[1328]
    print("The air quality is:", air_quality)
