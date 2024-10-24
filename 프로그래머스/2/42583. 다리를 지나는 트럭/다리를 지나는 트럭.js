function solution(num, w, arr) {
    let time=0
    let bridge= new Array(num).fill(0);
    
    while(arr.length!=0){
        time +=1
        bridge.shift()
        let sum_bridge = bridge.reduce((a, c) => a + c,0);
        if (sum_bridge + arr[0] <= w) bridge.push(arr.shift())
        else bridge.push(0)
    }
    time += num
    return time
}