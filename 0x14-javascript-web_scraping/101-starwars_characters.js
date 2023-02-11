#!/usr/bin/node
const req = require('request');
const fetchUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req(fetchUrl, (err, res, data) => {
  if (err) console.log(err);
  else {
    JSON.parse(data).characters.sort().forEach(ch => {
      req(ch, (err, res, data) => console.log(err || JSON.parse(data).name));
    });
  }
});
