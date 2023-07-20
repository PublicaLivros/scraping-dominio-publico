#!/bin/bash

feedback="init"

function execute() {
    local executecommand=$1
    if [[ executecommand -eq 1 ]]; then
        echo "Doing web scraping of the website data..."
        node ./js/scraping.js
    elif [[ executecommand -eq 2 ]]; then
        echo "Downloading the books using the obtained scraping..."
        if [[ -e "./json/raw_data.json" ]]; then python ./python/download.py;
        else echo "Oops, you didn't do the scraping!";
        fi
    elif [[ executecommand -eq 3 ]]; then
        echo "Removing raw_data.json..."
        if [[ -e "./json/raw_data.json" ]]; then rm ./json/raw_data.json;
        else echo "Scraping data doesn't exist";
        fi
    elif [[ executecommand -eq 4 ]]; then
        echo "Removing all books from booklibrary..."
        if [[ -d "./booklibrary" ]]; then rm ./booklibrary/*;
        else echo "There are no books saved here.";
        fi
    else
        return 1
    fi
}

function showMenu() {
    echo -e "SCRAPPING - PUBLIC DOMAIN: 
1) NodeJS scraping for raw_data.
2) Download books from raw_data scraping.
3) Remove raw_data scraping.
4) Remove all books from "booklibrary".
help) Help about this script.
"
    echo "$feedback"
    echo -n "Choose: "
    read -r usrinput
    clear
    testInput $usrinput
    feedback=""
}

function testInput() {
    case $1 in
        1)
            execute 1
        ;;
        2) 
            execute 2
        ;;
        3) 
            execute 3
        ;;
        4) 
            execute 4
        ;;
        help)
            echo "Is it so complicated to press a button?"
        ;;
        *)
            clear
            if [[ $feedback != "init" ]]; then feedback="Command not found."; fi
            if [[ $feedback == "init" ]]; then feedback=""; fi
            showMenu
        ;;
    esac
}

testInput $1
