#!/usr/bin/node
const { argv } = require('process');

const arr = argv.slice(2);
if (arr.length < 2) { console.log(0); } else {
  const digits = arr.map((e) => +e).sort((a, b) => a - b);
  console.log(digits[digits.length - 2]);
}
