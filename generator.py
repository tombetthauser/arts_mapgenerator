import geopandas
import folium
import pandas
import geopy
import os

os.system('clear')
print('\n\nWelcome to the open arts map builder! If an error occurs check the formatting of your data.csv file and try running the generator.py file again.')
print('\nThe map generator will begin building your map momentarily...\n\n')
# os.system("sleep 5")
os.system("clear")

dataframe = pandas.read_csv("data.csv")
# cities = []
# names = {}
# websites = {}
# userinput = False

# os.system('clear')
# print('\n\nWelcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.\n')
# print('First, please enter the full case-sensitive text of what you want your websites title to be. Be careful with special charactors as they may break the website builder (if so you can always just start over by running this again).')
# title = input('\nYour web map title: ')

# os.system('clear')
# while userinput not in ('done', 'finished', 'complete', 'next', ''):
#   userinput = input(
#       "\n\nPlease enter an artist's studio location (address, city, country): ")
#   cities.append(userinput)
#   if userinput in ('done', 'finished', 'complete', 'next', ''):
#     break
#   userinput = input("Please enter that artist's name: ")
#   names[cities[len(cities)-1]] = userinput
#   if userinput in ('done', 'finished', 'complete', 'next', ''):
#     break
#   userinput = input("Please enter that artist's website: ")
#   websites[cities[len(cities)-1]] = userinput
#   os.system('clear')

# locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
# location = locator.geocode(cities[0])

try:
  map = folium.Map(location=[0, 0], zoom_start=14, tiles="CartoDB asspositron")
except:
  map = folium.Map(location=[0, 0], zoom_start=14)

# map = folium.Map(location=[location.latitude, location.longitude], zoom_start=14, tiles="CartoDB positron")
# for c in cities:
#   location = locator.geocode(c)
#   map3.add_child(folium.Marker(location=[location.latitude, location.longitude], popup=f"{names[c]}'s' Studio\n{websites[c]}", icon=folium.Icon(color='blue')))

map.save("index.html")

# f = open("your_artsmap.html", "r")
# contents = f.readlines()
# f.close()

# contents.insert(
#     37, f"<div class = 'user-title-div' style = 'text-align: center; height: 200px; font-size: 25px; line-height: 200px;'>{title}</div>")

# f = open("your_artsmap.html", "w")
# contents = "".join(contents)
# f.write(contents)
# f.close()

os.system('clear')
os.system('git add -A')
os.system("git commit -m 'Update to open_artsmap'")
os.system("git push")

os.system('clear')
print("\n\nYour map index.html file is complete! Your GitHub repo has also been automatically updated.")
print("\nYou now have a fully formatted and functional HTML file with the temporary title 'index.html' so it opens up as the automatic homepage of any folder you put it in. If you know a little HTML you can edit and style this file freely, it's not dependant on anything except the open source map resource its referencing online.")
print("\nThanks for using the open arts map generator! The generator will automatically open your map in your default browser and quit momentarily...\n\n")
# os.system("sleep 10")
os.system('clear')
os.system('open index.html')



