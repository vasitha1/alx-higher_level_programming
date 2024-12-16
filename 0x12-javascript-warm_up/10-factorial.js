#!/usr/bin/node

const args = process.argv;
let factorial = 1;
const num = parseInt(args[2], 10);

for (let i = num; i > 0; i--) {
  factorial *= i;
}
console.log(factorial);
