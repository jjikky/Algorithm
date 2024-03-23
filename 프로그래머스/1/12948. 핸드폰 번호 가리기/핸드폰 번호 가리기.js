function solution(s) {
    let len = s.length;
    return '*'.repeat(len-4)+ s.substr(len-4,len)
}