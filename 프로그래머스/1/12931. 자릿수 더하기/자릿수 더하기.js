function solution(n)
{
    
    let answer = String(n).split('').reduce((a,c)=>{ return Number(a)+Number(c)},0)
    return answer;
}