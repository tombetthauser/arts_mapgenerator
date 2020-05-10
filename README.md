# Arts Map Generator
### A Python-Based Map Website Generator for Artists

Welcome to the arts map generator, a way for artists, galleries and arts institutions to make and host free fully interactive and mobile-friendly map websites to assist in promoting arts events like open studios or exhibition opening receptions.

***

To build your own arts map website follow these steps:
1. make a GitHub account or sign into your account
2. follow GitHub's instructions to clone this project
3. open your command line (Terminal on MacOS) and enter the cloned project folder
4. run the **installer.sh** script file by entering the code below into your command prompt
5. alternatively install Python3 Pip3 and install the Pandas, GeoPandas, Folium and Geopy Python libraries manually
```
  bash installer.sh
```
6. open the **data.csv** file and enter the information for your map
7. make sure to follow the formatting provided in the example data
8. finally run the **generator.py** map builder by entering the following into the command line
```
  python3 generator.py
```
9. your map will pop open automatically when it's complete
10. check to see that everything looks correct
11. if you find errors fix them in your **data.csv** file and then run your **generator.py** file again
12. your old map will automatically be replaced by the new one
  
  (instructions continued...)

***
## A Sample Arts Map Website  

![A Sample Map](image.png)  
[click here to check out the sample map](https://tombetthauser.github.io/python_map/index.html)
***  

13. each time you run **generator.py** your GitHub will also be automatically updated  
14. when you're satisfied go to the settings for your project on the GitHub website
15. go into the settings for this project and turn on GitHub pages near the bottom
16. this will give you a stand-alone link for your website
17. play around with your index.html file as much as you'd like, you can find great tutorials for HTML, CSS and JavaScript on **https://www.w3schools.com/** or **https://www.freecodecamp.org/**
18. whenever you want to update your map simply change your **data.csv** file and then run your **generator.py** file again  
```
  Your map website's is 100% yours, go share it with the world! 🎉
```  
***  
# Project Details
![python logo](https://docs.humio.com/integrations/python.svg)  

This project was built with **Python** using the **pandas**, **geopandas**, **folium**, **geopy** and **os** libraries to interface with the csv data, connect with the open source map reources underpinning the maps functionality and construct the automated **HTML** **CSS**, and **JavaScript** that constitutes the final product index.html file. The installer file was written specifically for this project in **bash** shell script.

This was originally developed as two day project by [Tom Betthauser](http://www.tombetthauser.com/) in 2020.  

***
