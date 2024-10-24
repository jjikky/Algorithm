function solution(prior, loc) {
    let answer=0
    let arr= Array.from({length:prior.length},(v,i)=>i+"");
    const target = arr[loc]
    while(arr){
        now = arr.shift();
        now_prior = prior.shift();
        max_prior = prior.reduce((max, current) => (current > max ? current : max), prior[0]);
        if(now_prior< max_prior){
            arr.push(now)
            prior.push(now_prior)
        }else{
            answer+=1
            if(now==target){
                break
            }
        }
    }
    return answer
}