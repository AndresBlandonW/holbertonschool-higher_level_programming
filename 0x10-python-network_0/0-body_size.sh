#!/bin/bash
# Takes in a URL, sends a request and display rhe size of body
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
