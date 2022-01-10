#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL and display the body of the response
curl -sX POST "$1" -F "email=test@gmail.com" -F "subject=I will always be here for PLD"
