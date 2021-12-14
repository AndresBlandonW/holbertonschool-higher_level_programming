#!/usr/bin/node
function add (a, b) {
  if (!isNaN(process.argv[3]) && process.argv[3] && !isNaN(process.argv[2]) && process.argv[2]) {
    console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
  }
}

add();
