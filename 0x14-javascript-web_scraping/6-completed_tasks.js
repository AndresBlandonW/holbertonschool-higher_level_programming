#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const res = tasks[i];
      if (res.completed === true) {
        if (completed[res.userId] === undefined) {
          completed[res.userId] = 1;
        } else {
          completed[res.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
