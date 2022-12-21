#!/usr/bin/node
const dict = require('./101-data').dict;
const obj = {};
for (const key in dict) {
  if (obj[dict[key]] === undefined) {
    obj[dict[key]] = [];
  }
  obj[dict[key]].push(key);
}

console.log(dict);
console.log(obj);
