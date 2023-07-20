#!/bin/bash

function execute() {
    local executecommand=$1
    if [[ executecommand -eq 1 ]]; then
        echo "Doing web scraping of the website data..."
        node ./js/scraping.js
    elif [[ executecommand -eq 2 ]]; then
        echo "Downloading the books using the obtained scraping..."
        if [[ -e "./json/raw_data.json" ]]; then
            python ./python/download.py
        else
            echo "Oops, you didn't do the scraping!"
        fi
    else
        return 1
    fi
}

function showMenu() {
    echo -e "SCRAPPING - PUBLIC DOMAIN: 
1) NodeJS scrapping for raw_data.
2) Download books from raw_data scrapping.
help) Help about this script.
"
echo -n "Choose: "
read -r usrinput
testInput $usrinput
}

function testInput() {
    case $1 in
        1)
            execute 1
        ;;
        2) 
            execute 2
        ;;
        help)
            echo "Is it so complicated to press a button?"
        ;;
        *)
            clear
            echo "Command not found."
            showMenu
        ;;
    esac
}

testInput $1
