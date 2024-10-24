function solution(s){
    let answer = true;
    const arr = [];
    s.split('').forEach((v)=>{
        if(arr.length==0){
            arr.push(v);
        }else{
            // 다르면 매칭된거
            if(v!=arr.slice(-1)[0] && arr.slice(-1)[0]=='('){
                arr.pop()
            }else{
                arr.push(v)
            }
        }
        
    })
    
    if(arr.length>0)answer=false;
    

    return answer;
}