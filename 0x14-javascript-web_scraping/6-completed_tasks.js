#!/usr/bin/node
const req = require('request');
req(process.argv[2], (err, res, data) => {
  if (err) console.log(err);
  else {
    const ids = {};
    JSON.parse(data).forEach(todo => {
      if (todo.completed && ids[todo.userId]) ids[todo.userId]++;
      else if (todo.completed) ids[todo.userId] = 1;
    });

    console.log(ids);
  }
});
