if [ -n "$(pip3 list --disable-pip-version-check | grep -Fw colorama)" ]
then
echo "Colorama is installed!"
else
echo "Package -colorama- is not installed. Do you want to install it? (y/n)"
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
pip3 install colorama
fi
fi

if [ -n "$(pip3 list --disable-pip-version-check | grep -Fw requests)" ]
then
echo "Requests is installed!"
else
echo "Package -requests- is not installed. Do you want to install it? (y/n)"
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
pip3 install requests
fi
fi