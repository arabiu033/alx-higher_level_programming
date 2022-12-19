#!/usr/bin/node
const { argv } = require('process');

function fac (val) {
  if (val <= 1) { return 1; }
  return val * fac(val - 1);
}

console.log(fac(isNaN(+argv[2]) ? 1 : +argv[2]));
