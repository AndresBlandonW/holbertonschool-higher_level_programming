#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let row = '';
    for (let x = 0; x < process.argv[2]; x++) {
      row += 'X';
    }
    console.log(row);
  }
}
