"""
Created by: Anthony Herrera
Purpose: Shows when the ISS will pass over Des Moines Iowa
Notes: following tutorial for the basics
https://www.dataquest.io/blog/python-api-tutorial/
This tutorial will be using OpenNotify API to get data about NASA
"""

import requests
from datetime import datetime

# Change this for a different location
latitude = 41.5868
longitude = -93.6250

# Number of passses to return
number_of_pass = 6

# Pass as dictionary because requests can take care of formatting this way
parameters = {"lat": latitude, "lon": longitude, "n":number_of_pass}

response = requests.get("http://api.open-notify.org/iss-pass.json",
                         params=parameters)

data = response.json()['response']


print(data)
for single_pass in data:
    converted_time = datetime.utcfromtimestamp(single_pass['risetime']).strftime('%Y-%m-%d %H:%M:%SZ')
    single_pass['risetime'] = converted_time
    print(single_pass)
