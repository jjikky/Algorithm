function solution(n) {
    let answer;
    
    if (Math.sqrt(n)-Number.parseInt(Math.sqrt(n))==0)answer=(Math.sqrt(n)+1)**2
    else answer=-1
    return answer;
}