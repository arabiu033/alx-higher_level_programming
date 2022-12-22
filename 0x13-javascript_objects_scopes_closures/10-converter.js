#!/usr/bin/node

exports.converter = function (base) {
  this.base = base;
  this.func = (num) => num.toString(this.base);
  return this.func;
};
