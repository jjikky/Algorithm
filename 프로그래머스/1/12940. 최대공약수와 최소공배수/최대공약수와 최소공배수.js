const solution = (n, m) => {
    return [uclid_gcd(n,m),lcm(n,m)];
}

const lcm = (n,m) => {
    // 두 수를 나눴을 때 0이 되는 가장 작은 수
    for(let i=2; i<=n*m; i++){
        if(i%n===0&&i%m===0) return i;
    }
}

const uclid_gcd = (n,m) =>{
    // gcd(n, m) = GCD(m, n%m)
    while(m > 0){
        let r = n % m;
        n = m;
        m = r;
    } 

    return n;
}


