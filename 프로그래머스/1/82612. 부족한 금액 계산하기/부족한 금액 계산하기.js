function solution(price, money, count) {
    let pay = 0;
    for(let i=1; i<=count; i++){
        pay+= price*i;
    }
    let answer = pay-money<=0 ? 0 : pay-money
    return answer;
}