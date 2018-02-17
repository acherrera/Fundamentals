#!/bin/bash
# Simple script to create a file with the current date

if [ -z "$1" ]
then
    echo No descriptor provide
else
    mkdir $( date -I'date' )-$1
fi
