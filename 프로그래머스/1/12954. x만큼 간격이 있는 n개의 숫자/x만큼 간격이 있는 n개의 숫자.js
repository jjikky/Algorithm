function solution(x, n) {
    var answer = [];
    now=n
    while(now--){
        answer.push(x+x*(n-now-1))
    }
    return answer;
}