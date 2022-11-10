echo "Installing pymoon"



if [ $(ls | grep pymoon.py) == "pymoon.py" ] 
then
    echo ""
else
    echo "Where is 'pymoon.py' "
    exit 1

fi


# install python3
echo "Installing Dependency"

sudo apt-get install python3

# Give permision file
chmod +x pymoon.py

# copy pymon to /bin/ for direct access
sudo cp pymoon.py /opt/

# link script
sudo ln /opt/pymoon.py /usr/bin/pymoon
