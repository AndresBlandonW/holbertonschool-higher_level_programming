#!/bin/bash
# Sends a DELETE request to the URL passed as the first arg and display th body of the response
curl -sX DELETE "$1"
