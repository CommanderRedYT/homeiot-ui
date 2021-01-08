function checkPIPinstall() {
    PCKG=$1
    if [ -n "$(pip3 list --disable-pip-version-check | grep -Fw $PCKG)" ]
    then
    echo "$PCKG is installed!"
    else
    echo "Package -$PCKG- is not installed. Do you want to install it? (y/n)"
    read -p "Are you sure? " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
    sudo pip3 install $PCKG
    else
    echo "This package is required for this to function!"
    exit
    fi
    fi
}
checkPIPinstall "colorama"
checkPIPinstall "requests"