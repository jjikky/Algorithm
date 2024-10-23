const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

input.forEach((row, i) => {
  arr = row.split(" ");
  avg_arr = (arr.reduce((acc, cur) => acc + cur * 1, 0) - arr[0] * 1) / arr[0];
  let count = 0;
  for (i = 1; i < arr.length; i++) {
    if (arr[i] > avg_arr) count += 1;
  }
  if (i != 1) {
    console.log(((count * 100) / arr[0]).toFixed(3) + "%");
  }
});
