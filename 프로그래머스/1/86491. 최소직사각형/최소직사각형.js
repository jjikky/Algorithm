function solution(sizes) {
    let arr = sizes.map((v)=>v.sort((a,b)=>b-a))
    let x=0,y=0
    
    arr.forEach(([a,b])=>{
        if(a>x)x=a
        if(b>y)y=b
    })
    
    return x*y
}