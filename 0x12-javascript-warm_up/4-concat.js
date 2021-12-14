#!/usr/bin/node
if (process.argv.length < 2) {
  console.log('undefined'.concat(' is ').concat('undefined'));
} else if (process.argv.length === 3) {
  console.log(process.argv[2].concat(' is ').concat('undefined'));
} else if (process.argv.length > 3) {
  console.log(process.argv[2].concat(' is ').concat(process.argv[3]));
}
