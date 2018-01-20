#!/usr/bin/bash

echo '----------------------------------------------------'
echo '              Installing virtualenv'
echo '----------------------------------------------------'
echo ''

#INSTALLING virutalenv
if virtualenv venv; then
    echo 'virtualenv installation success'
else
    echo 'virtual installation failed'
    exit;
fi

#Activating virtualenv bash source
source venv/bin/activate

#Installing pip requirements
echo '----------------------------------------------------';
echo '              Installing Requirements'
echo '----------------------------------------------------';
echo ''

if pip install -r requirements.txt; then
    echo 'requirements installed successfully'
else
    echo 'requirements installation failed'
fi

#setting up secret.py
cp app/secret.py.tempate app/secret.py

echo ''
echo 'PLEASE EDIT CONFIGURATIONS INSIDE app/secret.py'

echo ''
echo 'Installation successful'
