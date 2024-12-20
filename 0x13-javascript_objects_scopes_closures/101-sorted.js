#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const userId in dict) {
  const count = dict[userId];

  if (!newDict[count]) {
    newDict[count] = [];
  }
  newDict[count].push(userId);
}
console.log(newDict);
