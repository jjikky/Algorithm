function solution(n) {
    let sum = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) sum += i+(n/i==i?0:n/i)
    }
    return sum
}