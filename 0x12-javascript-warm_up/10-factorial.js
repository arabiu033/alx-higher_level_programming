#!/usr/bin/node
const { argv } = require('process');

function fibo (val) {
  if (val <= 1) { return 1; }
  return fibo(val - 1) + fibo(val - 2);
}

console.log(fibo(isNaN(+argv[2]) ? 1 : +argv[2]));
