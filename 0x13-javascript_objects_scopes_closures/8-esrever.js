#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    [list[i], list[j]] = [list[j], list[i]];
  }
  return list;
};
