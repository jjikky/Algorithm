let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let arrS = new Set(input.slice(1, N+1));
let arrM = input.slice(N+1);
let answer = 0;
for(let i=0; i<M; i++){
    if(arrS.has(arrM[i])) answer++
}
console.log(answer)