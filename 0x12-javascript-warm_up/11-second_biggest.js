#!/usr/bin/node

const args = process.argv;

let largestNum = 0;
let secondLarge = 0;

for (let i = 2; i < args.length; i++) {
  const num = parseInt(args[i], 10);
  if (num > largestNum) {
    secondLarge = largestNum;
    largestNum = num;
  }
}
console.log(secondLarge);
