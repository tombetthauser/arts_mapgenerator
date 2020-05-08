import os

os.system('clear')
print('\n\nWelcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.\n')
print('Before you begin please make sure you have Python3 and Pip3 installed on your machine.')
print("If you aren't sure how to do this just checkout the walkthough video linked on github, it's easy and straight forward!")
isContinue = input("\nIf you have these ready press enter to start, otherwise press Control + C to quit for now: ")

os.system('pip3 install folium')
os.system('pip3 install geopy')
os.system('pip3 install geopandas')

import folium
import geopy
import geopandas

cities = []
names = {}
websites = {}
userinput = False

os.system('clear')
print('\n\nWelcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.\n')
print('First, please enter the full case-sensitive text of what you want your websites title to be. Be careful with special charactors as they may break the website builder (if so you can always just start over by running this again).')
title = input('\nYour web map title: ')

os.system('clear')
print('\n\nNow start adding the names and addresses for your individual map locations (ie galleries, studios etc.)')
print('\nMake sure to enter addresses carefully or the map builder might crash (again, if it does crash no worries, just run this again from the start).')
print('Addresses hould be entered as such: "800 Chestnut Street, San Francisco, CA".')
print('When complete enter "done" or enter no information and the map builder will start making your website.')
print("\nWhen you're all done your browser will open a preview version of your map with all the locations you entered.")
input("When you're ready to start press enter, or Control + C to quit at any time. ")

os.system('clear')
while userinput not in ('done', 'finished', 'complete', 'next', ''):
  userinput = input("\n\nPlease enter an artist's studio location (address, city, country): ")
  cities.append(userinput)
  if userinput in ('done', 'finished', 'complete', 'next', ''):
    break
  userinput = input("Please enter that artist's name: ")
  names[cities[len(cities)-1]] = userinput
  if userinput in ('done', 'finished', 'complete', 'next', ''):
    break
  userinput = input("Please enter that artist's website: ")
  websites[cities[len(cities)-1]] = userinput
  os.system('clear')

print('\nAll addresses entered, please wait for map to be generated, it will open automatically.\n')

cities.pop()

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
location = locator.geocode(cities[0])

map3 = folium.Map(location=[location.latitude,location.longitude], zoom_start=14, tiles="CartoDB positron")
for c in cities:
  location = locator.geocode(c)
  map3.add_child(folium.Marker(location=[location.latitude, location.longitude], popup=f"{names[c]}'s' Studio\n{websites[c]}", icon=folium.Icon(color='blue')))

map3.save("Map3.html")

f = open("Map3.html", "r")
contents = f.readlines()
f.close()

contents.insert(37, f"<div class = 'user-title-div' style = 'text-align: center; height: 200px; font-size: 25px; line-height: 200px;'>{title}</div>")

f = open("Map3.html", "w")
contents = "".join(contents)
f.write(contents)
f.close()

os.system('open Map3.html')
