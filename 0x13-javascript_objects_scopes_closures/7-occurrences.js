#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((sum, e) => sum + (e === searchElement ? 1 : 0), 0);
};
