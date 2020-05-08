clear
printf "\n\nStarting installer ⏳...\n\n"
sleep 1

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor

brew install git
brew install python3
python3 get-pip.py

pip3 install geopandas
pip3 install folium
pip3 install geopy

clear
printf "\n\nInstaller finished! 👍\n\n"