#!/usr/bin/node
const p = require('process');
console.log(p.argv.length > 2 ? 'Argument found' : 'No argument');
