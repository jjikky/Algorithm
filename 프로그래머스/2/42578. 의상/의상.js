function solution(clothes) {
    let answer =1;
    let map = new Map();
    // 부위별 개수
    for([_,type] of clothes){
        v = map.get(type)
        v ? map.set(type,v+1):map.set(type,1)
    }
    // answer *= 부위별 개수 + 안입는 경우
    for(let [k,v] of map){
        console.log(k,v)
        answer*=v+1
    }
    // 모두 안입는 경우 배제
    return answer-1
}