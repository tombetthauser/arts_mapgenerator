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
addresses = list(dataframe["address"])
websites = list(dataframe["website"])
names = list(dataframe["name"])

os.system('clear')
print('\n\nWelcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.\n')
print('First, please enter the full case-sensitive text of what you want your map / website title to be.')
title = input('\nYour web map title: ')

os.system('clear')
subtitle = input('\n\nIf you would like some optional text below your main title enter it here. Otherwise leave this blank and hit enter: ')

os.system('clear')
mainlink = input('\n\nLastly, if you would like an optional website link below your subtitle text enter it here. Otherwise leave this blank and hit enter: ')

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')

split = addresses[0].split(', ')
lastele = split[len(split) - 1]
address = list(locator.geocode(lastele))
city = address[0].split(', ')[0]
location = locator.geocode(city)
loclist = [location.latitude - 0.0225, location.longitude]

try:
   map = folium.Map(location=loclist, zoom_start=13.25, tiles="CartoDB positron")
except:
   map = folium.Map(location=loclist, zoom_start=13.25)

for name, address, website in zip(names, addresses, websites):
  location = locator.geocode(address)
  loclist = [location.latitude, location.longitude]
  map.add_child(folium.Marker(
    location=loclist, 
    popup=f"<div style='width: 300px;'><h4>{name}</h4>\n{address}<br><a target='new' href='{website}'>{website}</a></div>", 
    icon=folium.Icon(color='blue')
  )
)

map.save("index.html")

f = open("index.html", "r")
contents = f.readlines()
f.close()

title = "Sacramento Arts Map"
subtitle = "Welcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions. For a quick and easy step-by-step guide on how to make your own arts map website and host it for free check out the readme file at the GitHub link below. This free tool is built using open source map and data libraries."
mainlink = "https://github.com/tombetthauser/open_artsmap"

if mainlink == "" and subtitle == "":
  html = (
    f"<div class='user-title-div' style='text-align: center; height: 200px; font-size: 25px; line-height: 200px;'>{title}</div>"
  )
elif mainlink == "":
  html = (
    "<div class='user-title-div' style='text-align: center; height: 300px; font-size: 25px; padding-top: 65px'>",
    f"{title}",
    "<div class='user-title-div' style='display: block; text-align: center; height: 100px; font-size: 15px; width: 500px; margin: 15px auto;'>",
    f"{subtitle}",
    "</div></div>",
  )
else:
  html = (
    "<div class='user-title-div' style='text-align: center; font-size: 25px; padding-top: 50px; padding-bottom: 40px'>",
    f"{title}",
    "<div class='user-title-div' style='display: block; text-align: center; font-size: 15px; width: 500px; max-width: 80%; margin: 15px auto;'>",
    f"{subtitle}",
    "</div>",
    f"<a target='new' style='font-size: 15px;' href={mainlink}>{mainlink}</a>",
    "</div>",
  )


contents.insert(37, "".join(html))

f = open("index.html", "w")
contents = "".join(contents)
f.write(contents)
f.close()

## Automatic GitHub Commit and Push
# os.system('clear')
# os.system('git add -A')
# os.system("git commit -m 'Update to open_artsmap'")
# os.system("git push")

os.system('clear')
print("\n\nYour map index.html file is complete! Your GitHub repo has also been automatically updated.")
print("\nYou now have a fully formatted and functional HTML file with the temporary title 'index.html' so it opens up as the automatic homepage of any folder you put it in. If you know a little HTML you can edit and style this file freely, it's not dependant on anything except the open source map resource its referencing online.")
print("\nThanks for using the open arts map generator! The generator will automatically open your map in your default browser and quit momentarily...\n\n")
# os.system("sleep 10")
os.system('clear')
os.system('open index.html')
