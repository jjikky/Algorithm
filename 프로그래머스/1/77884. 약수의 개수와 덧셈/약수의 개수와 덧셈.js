function solution(left, right) {
    let answer = 0;
    for(let i=left; i<=right; i++){
        let numDivisior = getDivisior(i);
        console.log(numDivisior);
        answer += numDivisior;
    }
    return answer;
}

function getDivisior(num){
    let cnt=0;
    for(i=1; i<=Math.sqrt(num); i++){
        if(i**2==num){
            cnt+=1;
        }
        else if(num%i==0){
            cnt+=2;
        }
    }
    if(cnt%2==0){
        return num
    }
    return num*-1;
}