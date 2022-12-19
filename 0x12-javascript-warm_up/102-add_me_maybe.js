#!/usr/bin/node
const obj = {
  addMeMaybe: (count, func) => {
    func(++count);
  }
};

module.exports = obj;
