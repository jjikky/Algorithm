function solution(genres, plays) {
    let map = new Map();
    genres.forEach((v,i)=>{
        map_v = map.get(v);
        map_v ? map.set(v,[...map_v,[plays[i],i]]) : map.set(v,[[plays[i],i]])
        if(map.get(v)?.length>1) map.get(v).sort((a,b)=>b[0]-a[0])
    })
    
    let sum_genre = []
    map.forEach((v,key)=>sum_genre.push([v.reduce((a,c)=>a+c[0],0),key]))
    sum_genre.sort((a,b)=>b[0]-a[0])
    
    let answer =[]
    for(let [sum_play,genre] of sum_genre){
        if(map.get(genre)[0]){
            answer.push(map.get(genre)[0][1])
        }
        if(map.get(genre)[1]){
            answer.push(map.get(genre)[1][1])
        }
    }
    
    return answer
}