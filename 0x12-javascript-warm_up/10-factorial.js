#!/usr/bin/node
function factorial (arg) {
  if (arg === 1 || isNaN(arg)) {
    return (1);
  }
  return (arg * factorial(arg - 1));
}

const arg = Number(process.argv[2]);
console.log(factorial(arg));
