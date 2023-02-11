#!/usr/bin/node
const req = require('request');
req(process.argv[2], (err, res) => console.log(err || `code: ${res.statusCode}`));
