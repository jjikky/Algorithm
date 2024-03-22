function solution(friends, gifts) {
    len = friends.length;
    names={}
    for(var i in friends)names[friends[i]]=i
    arr = Array.from({ length: friends.length }, () => Array.from({ length: friends.length }).fill(0));
    for(var x of gifts)arr[names[x.split(' ')[0]]][names[x.split(' ')[1]]]+=1
    give=new Array(len).fill(0);
    recieve = new Array(len).fill(0);
    for (let i=0; i<len; i++){
        give[i]=arr[i].reduce((a,b)=>a+b,0);
        for(let j=0; j<len; j++)recieve[i]+=arr[j][i];
    }
    let answer= new Array(len).fill(0);
    for (let i=0; i<friends.length; i++){
        for(let j=0; j<friends.length; j++){
            if (arr[i][j]>0 && arr[i][j] >arr[j][i])answer[i]+=1
            else if( arr[i][j]==arr[j][i] && give[i]-recieve[i]>give[j]-recieve[j])answer[i]+=1
        }
    }
    return Math.max.apply(null, answer);
}