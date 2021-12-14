#!/usr/bin/node
const arg = process.argv;
arg.splice(0, 2);

if (arg.length > 3) {
  arg.sort(function (a, b) { return b - a; });
  console.log(arg[1]);
} else {
  console.log(0);
}
