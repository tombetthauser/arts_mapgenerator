import geopandas
import geopy
import folium
import os

os.system('clear')
print('\n\nWelcome to the open arts map builder! If an error occurs check the formatting of your data.csv file and try running the generator.py file again.')
print('\nThe map generator will begin building your map momentarily...\n\n')
os.system("sleep 5")
os.system("clear")

# cities = []
# names = {}
# websites = {}
# userinput = False

# os.system('clear')
# print('\n\nWelcome to the open arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.\n')
# print('First, please enter the full case-sensitive text of what you want your websites title to be. Be careful with special charactors as they may break the website builder (if so you can always just start over by running this again).')
# title = input('\nYour web map title: ')

# os.system('clear')
# print('\n\nNow start adding the names and addresses for your individual map locations (ie galleries, studios etc.). Make sure to enter addresses carefully or the map builder might crash (again, if it does crash no worries, just run this again from the start).')
# print('\nAddresses should be entered as such: "800 Chestnut Street, San Francisco, CA".')
# print("When you're all done entering locations enter 'done' or enter no information and the map builder will start making your website.")
# print("\nAfter a few second your map site will be built and your default browser will open a preview version of your map with all the locations you entered. At this point you can review it and check everything. If anything is missing or incorrect you can fix it easily by running through all this again but unfortunately you'll have to re-enter all your map information and locations. Sorry!")
# input("\nWhen you're ready to start entering locations press enter, or Control + C to quit at any time. ")

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

# print('\nAll addresses entered, please wait for map to be generated, it will open automatically.\n')

# cities.pop()

# locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')
# location = locator.geocode(cities[0])

# map3 = folium.Map(location=[location.latitude, location.longitude],
#                   zoom_start=14, tiles="CartoDB positron")
# for c in cities:
#   location = locator.geocode(c)
#   map3.add_child(folium.Marker(location=[location.latitude, location.longitude],
#                                popup=f"{names[c]}'s' Studio\n{websites[c]}", icon=folium.Icon(color='blue')))

# map3.save("your_artsmap.html")

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
os.system("sleep 10")
os.system('clear')
# os.system('open index.html')



