echo "Installing pymoon"
echo "\n"



if [ $(ls | grep pymoon.py) == "pymoon.py" ] 
then
    echo ""
else
    echo "Where is 'pymoon.py' "
    exit 1

fi


pythonExist =  $(python3 --version)


# installing python if not installed
{
    

} || {
    pip install python3

}