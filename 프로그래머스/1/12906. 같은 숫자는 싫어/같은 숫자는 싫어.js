function solution(arr) {
    let answer = [];
    for (let i of arr) {
        if (answer.slice(-1)[0] === i) continue;
        answer.push(i);
    }
    return answer;
}