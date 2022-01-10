#!/usr/bin/node
const arg = process.argv.slice(2);
let big = 0;
if (arg.length > 1) {
  arg.sort((a, b) => a - b);
  big = arg[arg.length - 2];
}
console.log(big);
