const solution = (num)=>{
    answer = [0,90,91,180].filter(x => num >= x).length
    return answer
}