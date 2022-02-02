#!/usr/bin/node
const fs = require('fs');
const file = process.arg[2];
fs.eadFile(file, 'utf-8', function (err, data) {
    if (err) {
	console.log(err);
    } else {
	console.log(data);
    }
});
