#!/usr/bin/node
const p = require('process');
console.log(isNaN(+p.argv[2]) ? 'Not a number' : `My number: ${+p.argv[2]}`);
