#!/usr/bin/node
const request = require('request');
const eurl = process.argv[2];
request(eurl, function (error, response) {
  console.log('code:', response && response.statusCode);
});
