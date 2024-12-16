#!/usr/bin/node

const args = process.argv;

const firstNum = parseInt(args[2], 10);
const secondNum = parseInt(args[3], 10);

function add (a, b) {
  return (a + b);
}
console.log(add(firstNum, secondNum));
