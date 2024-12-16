#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  if (args[2] > 0) {
    const x = parseInt(args[2], 10);
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
