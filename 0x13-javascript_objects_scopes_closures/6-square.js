#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c = 'X') {
    let str;
    for (let i = 0; i < this.height; i++) {
      str = '';
      for (let j = 0; j < this.width; j++) { str += c; }
      console.log(str);
    }
  }
};
