#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filep = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filep, body, 'utf-8');
  }
});
