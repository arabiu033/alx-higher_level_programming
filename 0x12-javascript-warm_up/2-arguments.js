#!/usr/bin/node
const p = require('process');
if (p.argv.length > 2) { console.log(p.argv.length === 3 ? 'Argument found' : 'Arguments found'); } else { console.log('No argument'); }
