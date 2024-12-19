#!/usr/bin/node

class Rectangle {
  // class defining a rectangle

  constructor (w, h) {
    if (!(w > 0) || !(h > 0)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const line = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
