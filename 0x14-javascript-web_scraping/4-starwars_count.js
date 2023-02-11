#!/usr/bin/node
const req = require('request');
req(process.argv[2], (err, res, data) => {
  if (err) console.log(err);
  else {
    const count = JSON.parse(data).results.reduce(
      (total, chs) => total + chs.characters.filter(ch => ch.includes('18')).length, 0);
    console.log(count);
  }
});
