// //입력 파일 전체 받아오기
// const fs = require("fs");
// let input = fs.readFileSync("./tc.txt").toString().trim();

// //입력 정제하기
// let [n, ...arr] = input;

// //문제 풀이 로직
// function solution(n, arr) {
//   let ans = 0;
//   console.log(n, arr);
//   return ans;
// }

// solution(n, arr);

/* 입력 파일 형태
5 8 3
2 4 5 4 6
*/

// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); //줄바꿈 처리 추가

// let [nums, arr] = input;
// console.log(nums, arr); //5 8 3 2 4 5 4 6

// let [n, m, k] = nums.split(" ").map((value) => +value); //공백 날리고 숫자로 변경
// arr = arr.split(" ").map((value) => +value);
// console.log(n, m, k); //5 8 3
// console.log(arr); //[2, 4, 5, 4, 6]
