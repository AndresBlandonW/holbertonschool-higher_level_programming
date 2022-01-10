#!/bin/bash
# Takes in a URL as an arg sends a GET request to the URL and display the bdy of the resp
curl "$1" -sH "X-School-User-Id:98"
