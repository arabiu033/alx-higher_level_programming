#!/usr/bin/node
const p = require('process');
console.log(p.argv[2] === undefined ? 'No argument' : p.argv[2]);
