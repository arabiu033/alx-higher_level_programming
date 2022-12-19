#!/usr/bin/node
const obj = {
  callMeMoby: (count, func) => {
    for (let i = 0; i < count; i++) { func(); }
  }
};

module.exports = obj;
