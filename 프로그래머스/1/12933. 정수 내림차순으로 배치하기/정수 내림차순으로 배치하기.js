function solution(n) {
    let s = String(n)
    arr=[];
    for(i of s){
        arr.push(i)
    }
    arr.sort().reverse();
    let answer = '';
    for(i of arr){
        answer+=i
    }
    return Number(answer);
}