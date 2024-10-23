function solution(p, s) {
    let answer = [];
    let day = 0;
    let cnt = 0;

    while (p.length > 0) {
        if (p[0] + day * s[0] >= 100) {
            s.shift();
            p.shift();
            cnt++;
        } else {
            day++;
            if (cnt > 0) {
                answer.push(cnt);
                cnt = 0;
            }
        }
    }
    answer.push(cnt);
    return answer;
}
