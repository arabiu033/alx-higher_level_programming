#!/usr/bin/node
const { exit, argv } = require('process');

if (isNaN(+argv[2])) {
  console.log('Missing size');
  exit();
}

let str;
for (let i = 0; i < +argv[2]; i++) {
  str = '';
  for (let j = 0; j < +argv[2]; j++) { str += 'X'; }
  console.log(str);
}
