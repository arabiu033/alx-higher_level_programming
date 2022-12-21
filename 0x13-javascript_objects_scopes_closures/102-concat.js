#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], (_, data) => { fs.appendFile(argv[4], data.toString(), (_) => {}); });
fs.readFile(argv[3], (_, data) => { fs.appendFile(argv[4], data.toString(), (_) => {}); });

