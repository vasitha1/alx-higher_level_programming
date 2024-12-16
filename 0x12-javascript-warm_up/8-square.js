#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  const myNum = parseInt(args[2], 10);
  const line = 'X'.repeat(myNum);
  for (let i = 0; i < myNum; i++) {
    console.log(line);
  }
}
