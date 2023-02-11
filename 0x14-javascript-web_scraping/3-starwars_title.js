#!/usr/bin/node
const req = require('request');
const fetchUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req(fetchUrl, (err, res, data) => console.log(err || JSON.parse(data).title));
