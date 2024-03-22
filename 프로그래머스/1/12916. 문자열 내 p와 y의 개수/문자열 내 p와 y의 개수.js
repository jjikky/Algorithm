function solution(s){
    var answer = true;
    let [p,y]=[0,0];
    for(let i of s){
        if(i.toLowerCase()=='p')p+=1
        else if(i.toLowerCase()=='y')y+=1
    }
    if(p!=y)answer=false;
    return answer;
}