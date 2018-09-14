"""
Purpose: Show the number of people in space.
Created by: Anthony Herrera
Notes: Following a tutorial. Same as first file. Made changes afterwards to make
is print a litte better
"""

import requests

response = requests.get("http://api.open-notify.org/astros.json")
# Converts from JSON object to list or dictionary
data = response.json()

number_of_people = data['number']
people_info = data['people']


print("There are {} people in space".format(number_of_people))
for i in people_info:
    craft = i['craft']
    name = i['name']
    print("{} is on {}".format(name, craft))
