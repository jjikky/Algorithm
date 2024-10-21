const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

input.shift();
let arr = [...new Set(input)];
arr = arr.sort((a, b) => a.length - b.length || a.localeCompare(b)).join("\n");
console.log(arr);
