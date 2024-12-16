#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2], 10);

function factor (n) {
  if (n === 0 || isNaN(n) === true) {
    return 1;
  }
  return (n * factor(n - 1));
}
console.log(factor(num));
