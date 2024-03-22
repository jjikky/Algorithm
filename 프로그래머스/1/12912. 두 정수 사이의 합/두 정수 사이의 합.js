function solution(a, b) {
    answer=0;
    if(a>b){
        [a,b]=[b,a]
    }
    for(let v=a; v<=b; v++ ){
        answer+=v;
    }
    return answer;
}